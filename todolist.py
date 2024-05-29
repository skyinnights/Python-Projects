import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x400")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.save_button = tk.Button(master, text="Save", command=self.save_tasks)
        self.save_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        self.load_button = tk.Button(master, text="Load", command=self.load_tasks)
        self.load_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                for task in self.tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            self.clear_tasks()
            with open(file_path, "r") as file:
                for line in file:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
            messagebox.showinfo("Success", "Tasks loaded successfully.")

def main():
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
