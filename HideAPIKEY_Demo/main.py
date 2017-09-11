import password
import requests
import json

from password import GOOGLE_API_KEY
gkey = GOOGLE_API_KEY

target_city = "Seattle, Washington"

# Build URL using the Google Maps API
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city, gkey)

print("\r\nDrill #1")
print(target_url)

# Run request
seattle_geo = requests.get(target_url).json()

# Extract Lat/Lng
lat = seattle_geo["results"][0]["geometry"]["location"]["lat"]
lng = seattle_geo["results"][0]["geometry"]["location"]["lng"]

# Print results
print("%s: %s, %s" % (target_city, lat, lng))