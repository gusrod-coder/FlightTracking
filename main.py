from matrix import MatrixSimulator
import time
from FlightRadarAPI import FlightRadar24API


fr_api = FlightRadar24API()

bounds = fr_api.get_bounds_by_point(42.28574184424516, -83.71751929972811, 25000)
flights = fr_api.get_flights(bounds = bounds)
matrix = MatrixSimulator(128,64,15)


print(flights)







for flight in flights:
    flight_details = fr_api.get_flight_details(flight)
    flight.set_flight_details(flight_details)
    ("Flying to", flight.destination_airport_name)
    matrix.draw_text(f"Age:{flight.aircraft_age}",0,0)
    matrix.draw_text(f"Airline:{flight.airline_name}",0,20)
    matrix.draw_text(f"Plane:{flight.aircraft_code}",0,40)
    matrix.show()
    matrix.run()
    time.sleep(2)

