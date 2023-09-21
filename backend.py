import requests
API_key = "8248ecaa820379fc6369334a804fd79a"

def get_data(place,days=None):
    url =f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8*days]
    return filtered_data

if __name__=="__main__":
    print(get_data("Tokyo",3))
    print("hello")