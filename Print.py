from FlightRadarAPI import FlightRadar24API
fr_api = FlightRadar24API()

bounds = fr_api.get_bounds_by_point(42.28574184424516, -83.71751929972811, 15000)
flights = fr_api.get_flights(bounds = bounds)

for flight in flights:
    flight_details = fr_api.get_flight_details(flight)
    flight.set_flight_details(flight_details)
    print("Flying to", flight.destination_airport_name)
    print("Aircraft Age:", flight.aircraft_age)
    print("Airline:", flight.airline_name)
    print("Plane:", flight.aircraft_code)

matrix.show()
print(flights)