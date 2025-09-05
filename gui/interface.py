import tkinter as tk
from tkinter import scrolledtext
from core.chat import chat
from core.functions import get_time, get_date, tell_joke, calculate_expression, get_weather
from core.knowledge import load_knowledge, search_knowledge

knowledge_base = load_knowledge()

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S - Chatbot")
        self.root.geometry("500x600")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.insert_message("J.A.R.V.I.S", "Hello! I'm J.A.R.V.I.S. How can I assist you today?")

    def insert_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.insert_message("You", user_input)
        self.entry.delete(0, tk.END)

        response = self.process_input(user_input)
        self.insert_message("J.A.R.V.I.S", response)

    def process_input(self, user_input):
        lower_input = user_input.lower()

        if lower_input == "quit":
            self.root.quit()

        if "time" in lower_input:
            return get_time()
        elif "date" in lower_input:
            return get_date()
        elif "joke" in lower_input:
            return tell_joke()
        elif lower_input.startswith("calculate"):
            expression = user_input[9:].strip()
            return calculate_expression(expression)
        elif "weather in" in lower_input:
            city = lower_input.split("weather in")[-1].strip()
            return get_weather(city)
        elif "tell me about" in lower_input:
            return search_knowledge(user_input, knowledge_base)
        else:
            response = chat.respond(user_input)
            return response if response else "I didn't quite understand that."