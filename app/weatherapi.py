import requests, json 
def weather(city):
    try:
        api_key = "53c196e52c73e3a6ef246aba6c91c2cd"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"


        complete_url = base_url  + "q=" + city + "&appid=" + api_key
        response = requests.get(complete_url) 
        x = response.json() 

        if x["cod"] != "404":  
            y = x["main"]
            return y

        else: 
            return  0
    except: return 0