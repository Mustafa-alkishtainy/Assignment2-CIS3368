
##Mustafa Al-kishtainy
##professor Otoo 3368

import mysql.connector 
from mysql.connector import Error
import json
import requests


## This is where the user inserts the city info ##
city=input("Enter the city to find the weather: ") # state name input by user which goes into link below
print("\n")
## this is where the info the user inputs go ## using the ("Values for a single state on a specific date") API
weather=requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=eddbc569689018a78d26d07356e707c2" %city) # gets the state info & date from the user (line 40-41) and then goes into the API and get that specified state
json_weather = weather.json() ## assigning the Json link to a variable 
print(json_weather) ## user decides if they want to print all of the Json info for that state in terminal or not