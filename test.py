from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")

location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")

location = geolocator.reverse("23.8185045,90.3555421", language="en")
# print(location.address)

print(location.raw)


