from matrix import MatrixSimulator
from FlightRadarAPI import FlightRadar24API

import time

fr_api = FlightRadar24API()


reloadTime = 20
interval = 5
endWait = interval * 2
bounds = fr_api.get_bounds_by_point(42.28574184424516, -83.71751929972811, 10000)
flights = fr_api.get_flights(bounds = bounds)
matrix = MatrixSimulator(128,64,15)



print(flights)



def calculateExtraWait(numFlights):
    numFlights = len(flights)
    if(numFlights * interval <= reloadTime):
        return reloadTime
    else:
        return endWait


def processText(text, numSkips) -> str:
    print(text)
    output = ""
    for c in text:
        if(c != " " and numSkips > 0):
            output = output + c
        else:
            numSkips = numSkips - 1;
            return output;
    return output;
        
def show_flight(index=0):
    global flights
    if index >= len(flights):
        time.sleep(calculateExtraWait(len(flights)))
        flights = fr_api.get_flights(bounds = bounds)
        matrix.root.after(0,show_flight);
        print("flights reloaded")
    else:
        matrix.drawImage("Delta", 96,32)
        flight = flights[index]
        flight_details = fr_api.get_flight_details(flight)
        flight.set_flight_details(flight_details)

        matrix.clear()
        matrix.draw_text(processText(f"Age:{flight.aircraft_age}", 2), 0, 0)
        matrix.draw_text(processText(f"Airline:{flight.airline_name}", 1), 0, 20)
        matrix.draw_text(processText(f"Plane:{flight.aircraft_code}", 1), 0, 40)
        print("showing new")

        matrix.root.after(interval * 1000, show_flight, index + 1)


matrix.root.after(0, show_flight)
print("before matrix run")
matrix.run()
print("after matrix run")

while True:
    time.sleep(calculateExtraWait())
    matrix.root.after(0,show_flight);
    print("flights reloaded")


