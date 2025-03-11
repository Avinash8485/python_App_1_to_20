import requests


APIkey ="938c233b41bed2e83cccea52a850577a"

def get_data(place,days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"

    response = requests.get(url)


    data = response.json()
    filtered_data = data["list"]
    days_data = 8 * days
    filtered_data = filtered_data[:days_data]

    return filtered_data

if __name__=="__main__":
    result =get_data("London",3)
    print(result)
