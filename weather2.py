import requests
import sys
import json
import pandas

apikey = "6b970fab4b35817499b86ddcf0b2b437"
zipcode = sys.argv[1]
countrycode = sys.argv[2]

weather_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"

result = requests.get(weather_url)

outputfile = pandas.read_json(result.text)
outputfile.to_csv('output.csv')
