from geopy.geocoders import Nominatim


def parse_location_from_address():
    geo_locator = Nominatim(user_agent="specify_your_app_name_here")
    location = geo_locator.geocode("175 5th Avenue NYC")
    # print(location.address)
    # print((location.latitude, location.longitude))
    print(location.raw)


def get_address_from_latlng():
    geo_locator = Nominatim(user_agent="specify_your_app_name_here")
    location = geo_locator.reverse("23.8185045,90.3555421", language="en")
    print(location.raw)
