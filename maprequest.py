import os
import requests

MAP_REQUEST_API = os.getenv("MAP_REQUEST_API")
MAP_REQUEST_ENDPOINT = "http://open.mapquestapi.com/geocoding/v1/address"
FROM_LOCATION = None
TO_LOCATION = None


class MapRequest:
    def __init__(self):
        globals()['FROM_LOCATION'] = input("please enter the location from where you want to travel")
        self.from_coordinate = self.get_coordinates(location=FROM_LOCATION)
        globals()['TO_LOCATION'] = input("please enter the location to where you want to travel")
        self.to_coordinate = self.get_coordinates(location=TO_LOCATION)
        print(self.from_coordinate)
        print(self.to_coordinate)

    def get_coordinates(self, location):
        params_latlong = {
            "key": MAP_REQUEST_API,
            "location": location,
            "outFormat": "json"
        }
        response = requests.get(MAP_REQUEST_ENDPOINT, params=params_latlong)
        coordinates = response.json()
        latitude = coordinates["results"][0]["locations"][0]["latLng"]["lat"]
        longitude = coordinates["results"][0]["locations"][0]["latLng"]["lng"]
        latlong = str(latitude) + "," + str(longitude)
        return latlong
