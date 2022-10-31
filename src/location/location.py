import geocoder
# g = geocoder.ip('me')
# print(g.latlng)

class UserLocation:
    def __init__(self) -> None:
        self.location_instance = geocoder.ip('me')
        self.user_location = self.location_instance.latlng
        print(self.user_location)
        self.user_lat = self.user_location[0]
        self.user_long = self.user_location[1]

    def get_location(self):
        self.user_location = self.location_instance.latlng
        self.user_lat = self.user_location[0]
        self.user_long = self.user_location[1]

    def get_user_lat(self):
        return self.user_lat
    
    def get_user_long(self):
        return self.user_long