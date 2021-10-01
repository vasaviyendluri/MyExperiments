import requests
latitude=input("enter coordinare of latitude: ")
longitude=input("enter coordinates of longitude: ")
#
url='https://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&lon='+longitude+'&units=metric&appid=6e88b388029db8bc1d0acac48ad63d47'
response=requests.get(url=url)
weather_data=eval(response.text)
print(weather_data["main"]["temp"])