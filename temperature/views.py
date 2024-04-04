from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests, random, os, json
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

def get_room_data():
    data = open(f"{os.path.dirname(__file__)}/rooms.json","r")
    data_final = json.loads(data.read())
    data.close()
    return data_final

def write_room_data(data):
    with open(f"{os.path.dirname(__file__)}/rooms.json", "w") as file:
        json.dump(data, file)


def create_room(roomName, temperature, distanceFromKitchen):
    data = get_room_data()

    if roomName in data:
        return "already exists."

    data[roomName] = {"temperature":int(temperature),"distance_from_kitchen":int(distanceFromKitchen)}
    write_room_data(data)

def edit_room(roomName, temperature, distanceFromKitchen):
    data = get_room_data()

    if roomName not in data:
        return "doesn't exist."
    
    data[roomName] = {"temperature":int(temperature),"distance_from_kitchen":int(distanceFromKitchen)}
    write_room_data(data)

# Create your views here.
def index(request):
    error_parameter = request.GET.get('error', None)
    context = {"rooms":get_room_data(), "error_P":error_parameter}
    return render(request, 'temperature_index.html',context=context)

def show(request, id):
    data = get_room_data()
    if id in data:
        response = "proceed"
        name = id.lower().replace("_"," ")
        temperature = str(data[id]["temperature"]) + "°F"
        distanceFromKitchen = str(data[id]["distance_from_kitchen"]) + "FT"
    else:
        response = "doesnt_exist"
        name = id.lower().replace("_"," ")
        temperature = "NUL"
        distanceFromKitchen = "NUL"
    
    context = {"response":response,"name": name,"temperature":temperature,"distanceFromKitchen":distanceFromKitchen}
    return render(request, 'show.html',context=context)

def new(request):
    context = {"name":""}
    return render(request, 'new.html', context=context)

def create(request):
    name = request.POST.get('name', None)
    if name != None:
        name = name.lower()
    temp = request.POST.get('temperature', None)
    dist = request.POST.get('distance', None)
    if not (name == None or temp == None or dist == None):
        create_room(name, temp, dist)
    return render(request, 'temperature_index.html')

from django.http import JsonResponse

def edit(request, id):
    roomData = get_room_data()
    
    # if id not in roomData:
    #     response = "room doesn't exist"
    #     temperature = "NUL"
    #     distance = "NUL"
    #     context = {"response": response, "id": id, "temperature": temperature, "distanceFromKitchen": distance}
    #     return render(request, 'edit.html', context=context)
    
    if request.method == "GET":
        temperature = roomData[id]['temperature']
        distance = roomData[id]['distance_from_kitchen']
        context = {"response": "", "id": id, "temperature": temperature, "distanceFromKitchen": distance}
        return render(request, 'edit.html', context=context)
    
    elif request.method == "PUT":
        try:
            temp = request.PUT.get("temperature",111)
            dist = request.PUT.get("distance",111)
            edit_room(id, temp, dist)
            return JsonResponse({"success": True})  # Respond with JSON indicating success
        except Exception as e:
            edit_room(id,69,69)
            return JsonResponse({"success": False, "error": str(e)})  # Respond with JSON indicating failure



def update(request, id):
    context = {"id": id}
    # return render(request, 'update.html',context=context)
    # Redirect to index in python django
    return render(request, 'index.html')

def delete(request, id): # Delete request
    
    data = get_room_data()
    if id not in data:
        response = "item deleted already or item doesn't exist."
    else:
        response = "proceed"
        del data[id]
        write_room_data(data)
    context = {"response":response,"id": id}
    return render(request, 'delete.html', context=context)

