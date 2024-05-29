import requests
import tkinter as tk
from datetime import datetime

# Constants for configuration
API_URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
UPDATE_INTERVAL = 1000  # Update interval in milliseconds (1 second)

def update_price():
    """Fetch the latest Bitcoin price and update the labels."""
    try:
        # Attempt to fetch data from the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        price_usd = data.get("USD", "N/A")  # Get the price in USD or 'N/A' if not available
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        price_usd = "Error"  # Display 'Error' if there's an issue with the request

    current_time = datetime.now().strftime("%H:%M:%S")

    # Update the labels with the fetched data
    price_label.config(text=f"{price_usd} $")
    time_label.config(text=f"Updated at: {current_time}")

    # Schedule the function to run again after the specified interval
    root.after(UPDATE_INTERVAL, update_price)

def setup_ui(root):
    """Set up the GUI components."""
    root.configure(bg="#282c34")  # Set background color

    fonts = {
        "header": ("poppins", 24, "bold"),
        "price": ("poppins", 22, "bold"),
        "time": ("poppins", 18, "normal")
    }

    colors = {
        "text": "#61dafb",
        "price": "#21a0a0",
        "time": "#abb2bf"
    }

    # Create and pack the labels
    header_label = tk.Label(root, text="Bitcoin Price", font=fonts["header"], fg=colors["text"], bg="#282c34")
    header_label.pack(pady=20)

    global price_label
    price_label = tk.Label(root, font=fonts["price"], fg=colors["price"], bg="#282c34")
    price_label.pack(pady=20)

    global time_label
    time_label = tk.Label(root, font=fonts["time"], fg=colors["time"], bg="#282c34")
    time_label.pack(pady=20)

def main():
    """Main function to run the application."""
    global root
    root = tk.Tk()
    root.geometry("400x500")
    root.title("Bitcoin Price Tracker")

    # Set up the GUI components
    setup_ui(root)

    # Start fetching the Bitcoin price
    update_price()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
