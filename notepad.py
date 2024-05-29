from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

def save_file():
    """Save the contents of the text entry to a file."""
    new_file = asksaveasfile(mode='w', filetype=[('Text Files', '*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def open_file():
    """Open a text file and insert its contents into the text entry."""
    file = askopenfile(mode='r', filetype=[('Text Files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)  # Clear existing content
        entry.insert(INSERT, content)

def clear_file():
    """Clear the contents of the text entry."""
    entry.delete(1.0, END)

def main():
    """Main function to run the notepad application."""
    root = Tk()
    root.title("Notepad")
    root.geometry("400x400")
    root.config(bg="#f0f0f0")

    top_frame = Frame(root, bg="#f0f0f0")
    top_frame.pack(pady=5)

    open_button = Button(top_frame, text="Open", bg="white", command=open_file)
    open_button.pack(side=LEFT, padx=5)

    save_button = Button(top_frame, text="Save", bg="white", command=save_file)
    save_button.pack(side=LEFT, padx=5)

    clear_button = Button(top_frame, text="Clear", bg="white", command=clear_file)
    clear_button.pack(side=LEFT, padx=5)

    exit_button = Button(top_frame, text="Exit", bg="white", command=root.quit)
    exit_button.pack(side=LEFT, padx=5)

    global entry
    entry = Text(root, wrap=WORD, bg="white", font=("Arial", 12))
    entry.pack(padx=5, pady=5, expand=TRUE, fill=BOTH)

    root.mainloop()

if __name__ == "__main__":
    main()
