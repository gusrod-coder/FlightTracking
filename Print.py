from FlightRadarAPI import FlightRadar24API
fr_api = FlightRadar24API()

bounds = fr_api.get_bounds_by_point(42.28574184424516, -83.71751929972811, 10000)
flights = fr_api.get_flights(bounds = bounds)
print(flights)