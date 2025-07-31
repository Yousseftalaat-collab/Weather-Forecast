import tkinter as tk

import requests

API_KEY = "280fd12e249abcd15a0d82cfb4e33161"

def get_weather():
    city = location_entry.get()
    if city.strip() == "":
        temperature_value.config(text="")
        humidity_value.config(text="")
        wind_value.config(text="")
        pressure_value.config(text="")
        precip_value.config(text="")
        print("Cleared input → Cleared labels")
        return
    

    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)        
        data = response.json()               
            
        if data.get("cod") != 200:
            temperature_value.config(text="N/A")
            humidity_value.config(text="N/A")
            wind_value.config(text="N/A")
            pressure_value.config(text="N/A")
            precip_value.config(text="N/A")
            return


        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        weather_main = data["weather"][0]["main"]


        temperature_value.config(text=f"{temperature}°C")
        humidity_value.config(text=f"{humidity}%")
        wind_value.config(text=f"{wind_speed} km/h")
        pressure_value.config(text=f"{pressure} hPa")
        precip_value.config(text=f"{weather_main}")


    except Exception as e:
        print("Error:", e)


window = tk.Tk()
window.title("Weather Forecast")
window.geometry("450x500") 
window.resizable(True,True )  

location_label = tk.Label(window, text="Location:", font=("Arial",14))
location_label.grid(row=0, column=0, padx=5, pady=20)

location_entry = tk.Entry(window, width=25)
location_entry.grid(row=0, column=1, padx=10)

search_button = tk.Button(window, text="Search", command=get_weather)
search_button.grid(row=0, column=2, padx=10)

weather_frame = tk.Frame(window)
weather_frame.grid(row=1, column=0, columnspan=1, pady=20)

temperature_label_text = tk.Label(weather_frame, text="Temperature:", font=("Arial", 14))
temperature_label_text.grid(row=0, column=0, sticky="w", padx=10, pady=5)

temperature_value = tk.Label(weather_frame, text="  °C", font=("Arial", 14))
temperature_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)

humidity_label_text = tk.Label(weather_frame, text="Humidity:", font=("Arial", 14))
humidity_label_text.grid(row=1, column=0, sticky="w", padx=10, pady=5)

humidity_value = tk.Label(weather_frame, text="  %", font=("Arial", 14))
humidity_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)

wind_label_text = tk.Label(weather_frame, text="Wind Speed:", font=("Arial", 14))
wind_label_text.grid(row=2, column=0, sticky="w", padx=10, pady=5)

wind_value = tk.Label(weather_frame, text="   km/h", font=("Arial", 14))
wind_value.grid(row=2, column=1, sticky="w", padx=10, pady=5)

pressure_label_text = tk.Label(weather_frame, text="Pressure:", font=("Arial", 14))
pressure_label_text.grid(row=3, column=0, sticky="w", padx=10, pady=5)

pressure_value = tk.Label(weather_frame, text="   hPa", font=("Arial", 14))
pressure_value.grid(row=3, column=1, sticky="w", padx=10, pady=5)

precip_label_text = tk.Label(weather_frame, text="Precipitation:", font=("Arial", 14))
precip_label_text.grid(row=4, column=0, sticky="w", padx=10, pady=5)

precip_value = tk.Label(weather_frame, text="  %", font=("Arial", 14))
precip_value.grid(row=4, column=1, sticky="w", padx=10, pady=5)


window.mainloop()