import tkinter as tk
import requests
import time

# Constants for configuration
API_KEY = "fe6a04b8024ae2f4653763920502f213"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
BG_COLOR = "#282c34"
TEXT_COLOR = "#61dafb"
ERROR_COLOR = "#ff6b6b"


def get_weather(event=None):
    """Fetch weather data for the entered city and update the labels."""
    city = textfield.get()
    api_url = f"{BASE_URL}{city}&appid={API_KEY}"

    try:
        json_data = requests.get(api_url).json()

        if json_data.get("cod") != 200:
            raise ValueError(json_data.get("message", "Error fetching data"))

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset']))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"Max Temp: {max_temp}°C\n"
            f"Min Temp: {min_temp}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )

        label1.config(text=final_info, fg=TEXT_COLOR)
        label2.config(text=final_data, fg=TEXT_COLOR)

    except (requests.RequestException, ValueError) as e:
        label1.config(text="Error", fg=ERROR_COLOR)
        label2.config(text=str(e), fg=ERROR_COLOR)


def setup_ui(root):
    """Set up the GUI components."""
    root.configure(bg=BG_COLOR)

    font_title = ("poppins", 35, "bold")
    font_info = ("poppins", 15, "bold")

    # Create and pack the text field
    global textfield
    textfield = tk.Entry(root, font=font_title, justify='center')
    textfield.pack(pady=20)
    textfield.focus()
    textfield.bind('<Return>', get_weather)

    # Create and pack the labels
    global label1, label2
    label1 = tk.Label(root, font=font_title, bg=BG_COLOR)
    label1.pack()

    label2 = tk.Label(root, font=font_info, bg=BG_COLOR)
    label2.pack()


def main():
    """Main function to run the application."""
    global root
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Weather App")

    # Set up the GUI components
    setup_ui(root)

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
