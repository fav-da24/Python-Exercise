import location
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium
from opencage.geocoder import OpenCageGeocode

#taking input the phone number alongwith the country code
number = input("Enter the phone number with the country code: ")

#Parsing String to the Phone Number
phoneNumber = phonenumbers.parse(number)
Key = "57b2664d929e46c997989d4ef48a8b6a"

#printing the geolocation of the given number using the geocoder module
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("location : " + yourLocation)

#printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber, "en")
print("Service Provider : " + service)

#using Opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

#assigning the latitude and longitude value to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

#getting the map for the given latitude and longitude
myMap = folium.Map(location=[lat, lng],zoom_start = 9)

#adding a marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

myMap.save("Location.html")