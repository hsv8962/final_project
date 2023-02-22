import json, requests


class Weather:
    def __init__(self, city, appid):
        self.city = city
        self.appid = appid
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_temperature(self):
        url = f"{self.base_url}?q={self.city}&units=imperial&APPID={self.appid}"
        try:
            response = requests.get(url)
            unformated_data = response.json()
            print("******** CONNECTION SUCCESSFUL *********")
            temp = unformated_data["main"]["temp"]
            temp_min = unformated_data["main"]["temp_min"]
            temp_max = unformated_data["main"]["temp_max"]
            pressure = unformated_data["main"]["pressure"]
            humidity = unformated_data["main"]["humidity"]
            wind_speed = unformated_data["wind"]["speed"]
            return temp, temp_min, temp_max, pressure, humidity, wind_speed
        except requests.exceptions.RequestException:
                print(f"""\nCONNECTION UNSUCCESSFUL! 
Please try again later. Goodbye!
""")
                return quit()
        except (KeyError, json.JSONDecodeError):
               print("\nThat is not found. Please try again.")



def main():
    appid = "906b6939735602a519447e37a839d229"

    while True:
        city = input("Please enter a [city name] or [zip code] or [quit] to exit: ")
        if city.lower() == "quit":
            break
        weather = Weather(city, appid)
        weather_data = weather.get_temperature()

        if weather_data is not None:
            temp, temp_min, temp_max, pressure, humidity, wind_speed = weather_data
            print(f"""Here is the weather information for {city.title()}
Current temp: {temp}\N{DEGREE SIGN}F
Minimum temp: {temp_min}\N{DEGREE SIGN}F
Maximum temp: {temp_max}\N{DEGREE SIGN}F
Pressure: {pressure} inHG
Humidity: {humidity}%
Wind speed: {wind_speed} mph
            """)
        else:
            print(f"Failed to get weather data for {city}.")


if __name__ == '__main__':
    main()
