import requests
import tkinter as tk
from tkinter import messagebox
import os

API_KEY = "408e9360e69ca6aa2ee44495d7a627de"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        resp = requests.get(url, timeout=10)

        data = resp.json()

        if resp.status_code != 200:
            err_msg = data.get("message", "Unknown API error.")
            messagebox.showerror("Error", f"API error: {err_msg} (HTTP {resp.status_code})")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()
        wind = data["wind"].get("speed", 0)

        temperature_label.config(text=f"Temperature: {temp}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        condition_label.config(text=f"Condition: {condition}")
        wind_label.config(text=f"Wind Speed: {wind} m/s")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Network issue: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

def convert_temp():
    current_text = temperature_label.cget("text")
    try:
        if "°C" in current_text:
            value = float(current_text.split(":")[1].replace("°C", "").strip())
            fahrenheit = (value * 9/5) + 32
            temperature_label.config(text=f"Temperature: {fahrenheit:.2f}°F")
        elif "°F" in current_text:
            value = float(current_text.split(":")[1].replace("°F", "").strip())
            celsius = (value - 32) * 5/9
            temperature_label.config(text=f"Temperature: {celsius:.2f}°C")
    except Exception:
        messagebox.showinfo("Info", "No temperature to convert yet.")


# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("Weather App")
root.geometry("400x420")
root.config(bg="#e3f2fd")

title_label = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#e3f2fd")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=6)

button = tk.Button(root, text="Get Weather", font=("Arial", 13), command=get_weather, bg="#f6ef64")
button.pack(pady=6)

convert_button = tk.Button(root, text="Convert °C / °F", font=("Arial", 12), command=convert_temp, bg="#90f4f9")
convert_button.pack(pady=4)

temperature_label = tk.Label(root, text="Temperature:", font=("Arial", 13), bg="#e3f2fd")
temperature_label.pack()

humidity_label = tk.Label(root, text="Humidity:", font=("Arial", 13), bg="#e3f2fd")
humidity_label.pack()

condition_label = tk.Label(root, text="Condition:", font=("Arial", 13), bg="#e3f2fd")
condition_label.pack()

wind_label = tk.Label(root, text="Wind Speed:", font=("Arial", 13), bg="#e3f2fd")
wind_label.pack()

root.mainloop()