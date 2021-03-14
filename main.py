
##Mustafa Al-kishtainy
##professor Otoo 3368

import mysql.connector 
from mysql.connector import Error
import json
import requests

## THE CODE THAT GET THE USER INFO AND CONNECTES IT WITH DB ##
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try: 
        connection= mysql.connector.connect(
        host= host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
        print("connection successful")
    except Error as e:
        print(f"the error '{e}' occured" )
    return connection
## THE CODE THAT RUNS THE CODE WRITTEN FROM PYTHON TO THE SQL ##
def execute_query(connection, query):
    mycursor=connection.cursor()
    try:
        mycursor.execute(query)
        connection.commit()
        print("Query ran successfuly")
    except Error as e:
        print(f"the error '{e}' occured")
## THE CODE THAT GETS THE DATA FROM WORKBENCH INTO PYTHON ##
def read_query(connection, query):
    mycursor= connection.cursor()
    result= None
    try:
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result
    except Error as e:
        print(f"the error '{e}' occured")

################################# USER INFO THAT connects to workbench and AWS ###########################################
connection= create_connection("cis3368v1.cl3c9tgm8sn0.us-east-2.rds.amazonaws.com","admin","Daguy.jason.com","cis3368v1db")


## This is where the user inserts the city info ##
city=input("Enter the city to find the weather: ") # state name input by user which goes into link below
print("\n")
## this is where the info the user inputs go ## using the ("Values for a single state on a specific date") API
weather=requests.get("http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=eddbc569689018a78d26d07356e707c2" %city) # gets the state info & date from the user (line 40-41) and then goes into the API and get that specified state
json_weather = weather.json() ## assigning the Json link to a variable 
print(json_weather) ## user decides if they want to print all of the Json info for that state in terminal or not

## GETS CITY NAME TO PRINT
city_name= json_weather["name"]
print("the city is %s " %(city_name))
## GOES INTO MAIN IN THE API AND GET THE TEMP, FEELS LIKE, AND HUMIDITY
city_main= json_weather["main"]
temp= city_main["temp"]
print(temp)
feels_like = city_main["feels_like"]
print(feels_like)
humidity= city_main["humidity"]
print(humidity)



