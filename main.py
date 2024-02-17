import requests
import json
import os 

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=88fbf7f1998f493491641057232707&q={city}"  # got this link from weatherapi

response = requests.get(url)  # gets response based on the city, type str

# print(response.text)  # type string

weather_dic = json.loads(response.text) #turns to dict
temp_f = round(weather_dic["current"]["temp_f"])
temp_c = round(weather_dic["current"]["temp_c"])

os.system(f"say 'The Current Temperature in {city} is {temp_f} Fahrenheit and {temp_c} celcius'")

