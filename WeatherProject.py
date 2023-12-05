import requests
import PySimpleGUI as sg

API_KEY = 'b75ddaaeed0cac26e7405723281dc1ec' # My API Key
sg.theme('DarkBlue1') # Sets the theme for the GUI

# THIS PORTION OF CODE CREATES THE GUI
layout = [
 [sg.Text('Current Weather')],
 [sg.Text('Input your city'), sg.InputText(key='-CITY-'), sg.Button('Enter')], #Asks user to input city
 [sg.Text('Temp:'), sg.Text(key='-WEATHER-')], #Prints Temp in Farenheight
 [sg.Text('Condition:'),sg.Text(key='-DESCRIPTION-')] #Prints description of weather
 ]

window = sg.Window('Weather App', layout)

# Create a session object which provides persistance via cookies allowing the code to call the API faster
session = requests.Session()

headers = {'Accept-Encoding': 'gzip'}

while True:
 event, values = window.read()
 if event == sg.WIN_CLOSED: # Closes if user closes window
     break
 
# THIS PORTION OF CODE CHECKS IF THE CITY EXISTS ADN THEN RETURNS THE DATA TO THE GUI
 if event == 'Enter':
     city = values['-CITY-'] #Asocciates Input to Get Request
     URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
     response = session.get(URL, headers=headers)
     if response.status_code == 200: #If response code is 200 aka OK then the city is valid
        request = response.json()
        temp_k = request['main']['temp'] #Sets weather in Kelvin
        temp_f = ((temp_k - 273.15) * 1.8) + 32 # Converts Kelvin to Fahrenheit
        temp_f = round(temp_f, 1) # Rounds Fahrenheit up
        desc = request['weather'][0]['description'] #Sets Weather Description
        window['-WEATHER-'].update(temp_f) #Updates GUI Temp
        window['-DESCRIPTION-'].update(desc) #Updates GUI Weather Description
     else:
        sg.popup('Invalid city name. Please enter a valid city.')


window.close()