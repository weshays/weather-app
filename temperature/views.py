from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests, random
# Create your views here.

def getIPData():
    try:
        ip = requests.get("https://api.ipify.org/?format=text").text
        re = requests.get(f"https://ipapi.co/{ip}/json/", headers={"user-agent":f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/{random.randint(100,999)}.36"}).json()
        #return [str(re),ip,"32.6917","-117.1151"]
        return [re['city'],re["region_code"],re['latitude'],re['longitude']]   
    except Exception as e:
        return [e,"NUL","32.6917","-117.1151"]
def fetch_temperature_data(request = "172.12.246.61"):
    data = getIPData()
    first_URL = requests.get(f"https://api.weather.gov/points/{str(data[2])},{str(data[3])}").json()
    r = requests.get(first_URL['properties']['forecast']).json()["properties"]["periods"][0]
    city = data[0]
    region_code = data[1]
    temperature = r["temperature"]
    temperatureUnit = r["temperatureUnit"]
    relativeHumidity = r["relativeHumidity"]["value"]
    windSpeed = r["windSpeed"]
    windDirection = r["windDirection"]
    return [city,region_code,temperature,temperatureUnit,relativeHumidity,windSpeed,windDirection]

# Create your views here.
def index(request):
    context = {"fetch_temperature_data":fetch_temperature_data(request)}
    return render(request, 'temperature_structure.html',context=context)

