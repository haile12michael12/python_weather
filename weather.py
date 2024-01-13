import requests
import tkinter as tk

def fetch_weather():
    city =city_var.get()
    if city:
      api_key = "c6478a826e35105b76992cc2e10969e5"
      base_url=f"https://api.weatherstack.com/current?access_key={api_key}&query={city}"
      response=requests.get(base_url)
      data=response.json()

      if data.get("current"):
       temperature = data["current"]["tempereture"]
       description=data["current"]["weather_description"][0]
       weather_info=f"weather in {city.capitalize():\nTemprature:{temperature}c/nDescription:{description.capitalize()}}"
       weather_label.config(text=weather_info)

      else:
        weather_label.config(text="city not found")
    else:
      weather_label.config(text="enter a city")
# main window
root=tk.TK()
root.title("weather app")
root.geometry("400X250")

 # label for title
title_label =tk.Label(
root,
text="weather app" ,
font=("Helvetical",20))
title_label.pack()

#label for city entry
city_label=tk.Label(
root,
text="enter a city:",
font=("Helvetical",16))
city_label.pack()

#  input for city name
city_var=tk.stringvar()
city_entry=tk.entry(
root,
textvariable=city_var,
font=("Helvetical",16))
city_entry_label.pack()

# search buttin to fetch weather dat
search_button=tk.Button(
root,
text="search city",
command=fetch_weather,
font=("Helvetical",16))
search_button.pack()

# label to display weather information
weathe_label=tk.label(
root,
text=""
font=("Helvetical",16))
weather_label.pack()

#main loop
root.mainloop()

    