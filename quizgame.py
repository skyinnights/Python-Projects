import tkinter as tk
from tkinter import messagebox
import random

class QuizGameApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("500x400")
        self.master.config(bg="#ffdb1d")

        self.questions = questions
        self.correct_answers = 0
        self.current_question_index = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 16), bg="#ffdb1d", wraplength=450)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Arial", 12), width=30, bg="#ffffff", fg="#333333",
                               activebackground="#dddddd", activeforeground="#333333",
                               command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question['question'])
            random.shuffle(question['options'])
            for i in range(4):
                self.option_buttons[i].config(text=question['options'][i], bg="#ffea00", fg="#333333")
        else:
            self.show_result()

    def check_answer(self, option_index):
        question = self.questions[self.current_question_index]
        if question['options'][option_index] == question['answer']:
            self.correct_answers += 1

        self.current_question_index += 1
        self.next_question()

    def show_result(self):
        result_message = f"Quiz completed!\n\nYour score: {self.correct_answers}/{len(self.questions)}\n\n"
        messagebox.showinfo("Quiz Result", result_message)
        self.master.destroy()

# Sample quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "Charles Dickens"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "answer": "H2O"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who discovered penicillin?",
        "options": ["Alexander Fleming", "Isaac Newton", "Albert Einstein", "Marie Curie"],
        "answer": "Alexander Fleming"
    }
]

def main():
    root = tk.Tk()
    app = QuizGameApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
