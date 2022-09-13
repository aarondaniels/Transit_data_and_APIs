import urllib.request
import json

# request json file 
url = "https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip"
response = urllib.request.urlopen(url).read()
data = json.loads(response)

#write to console
print(data)