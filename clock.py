from tkinter import *
from tkinter.ttk import *
from time import strftime

def update_time():
    """Update the label with the current time."""
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, update_time)

def main():
    """Main function to run the clock application."""
    root = Tk()
    root.title("Clock")
    root.geometry("500x200")  # Increased width to fit the entire text
    root.configure(background="#f0f0f0")

    global label
    label = Label(root, font=("Arial", 60), foreground="purple", background="#f0f0f0")
    label.pack(pady=50)

    update_time()  # Start updating the time

    root.mainloop()

if __name__ == "__main__":
    main()
