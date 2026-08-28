from matrix import MatrixSimulator
from FlightRadarAPI import FlightRadar24API


fr_api = FlightRadar24API()

bounds = fr_api.get_bounds_by_point(42.28574184424516, -83.71751929972811, 10000)
flights = fr_api.get_flights(bounds = bounds)
matrix = MatrixSimulator(128,64,15)


print(flights)





def processText(text, numSkips) -> str:
    print(text)
    output = ""
    for c in text:
        if(c != " " and numSkips > 0):
            output = output + c
        else:
            numSkips = numSkips - 1;
            return output;
        
def show_flight(index=0):
    if index >= len(flights):
        matrix.root.destroy()
        return

    flight = flights[index]
    flight_details = fr_api.get_flight_details(flight)
    flight.set_flight_details(flight_details)

    matrix.clear()
    matrix.draw_text(processText(f"Age:{flight.aircraft_age}", 2), 0, 0)
    matrix.draw_text(processText(f"Airline:{flight.airline_name}"), 0, 20)
    matrix.draw_text(processText(f"Plane:{flight.aircraft_code}"), 0, 40)
    print("showing new")

    matrix.root.after(2000, show_flight, index + 1)


matrix.root.after(0, show_flight)
matrix.run()

