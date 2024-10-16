import requests
import sys
import json

apikey = "6b970fab4b35817499b86ddcf0b2b437"
zipcode = sys.argv[1]
countrycode = sys.argv[2]

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"

result = requests.get(weather_url)

if result.status_code == 200:
    parsed_json = json.loads(result.text)
    print(json.dumps(parsed_json,indent=4))
else:
    print(f"Error: {result.json()}")
