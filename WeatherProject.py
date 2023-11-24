import requests
import PySimpleGUI as sg

#This project uses OpenWeatherAPI Key

API_KEY = 'b75ddaaeed0cac26e7405723281dc1ec' #My API Key

#Theme for PySimpleGUI
sg.ChangeLookAndFeel('Reddit')
BG_COLOR = "#FFCC66" #sg.theme_text_color()
TXT_COLOR = "#000000" #sg.theme_background_color()
ALPHA = 0.8

CITY = input("Enter city you want weather for: ") #Asks for City
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
response = requests.get(URL) #GET Request

if response.status_code == 200: #Checks if  GET Request is OK
    data = response.json() #Stores data from GET Request
    temp = data['main']['temp'] #Stores Tempeture from GET Request
    desc = data['weather'][0]['description'] #Stores description of weather from GET Request
    print(f'Temperature: {(temp - 273.15) * 1.8 + 32} F') #I have to convert to F using this formula F = (K − 273.15) × 1.8 + 32
    print(f'Description: {desc}') #Prints the description of the Weather
else:
    print('Error fetching weather data') #If city is not typed properly thows error or if request dosent suceed
    
