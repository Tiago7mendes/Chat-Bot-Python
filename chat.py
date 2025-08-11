# J.A.R.V.I.S Chatbot Avançado
# Autor: Tiago Setti
# Bibliotecas necessárias: nltk

from nltk.chat.util import Chat, reflections
import datetime
import random

# Funções dinâmicas para respostas
def get_time(*args):
    return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

def get_date(*args):
    return f"Today's date is {datetime.datetime.now().strftime('%d/%m/%Y')}."

def tell_joke(*args):
    jokes = [
        "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
        "Why was the math book sad? Because it had too many problems.",
        "What do you call 8 hobbits? A hobbyte."
    ]
    return random.choice(jokes)

def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"The result is {result}."
    except:
        return "I couldn't calculate that, sorry."

# Pares de entrada e resposta
pairs = [
    [r"my name is (.*)", ["Hi %1, nice to meet you!"]],
    [r"(hi|hello|hey|holla|hola|oi|eai)", ["Hello there!", "Hi!", "Hey!", "Olá!", "E aí?"]],
    [r"how are you(.*)", ["I'm doing great, thanks for asking!", "I'm fine, and you?"]],
    [r"what is your name ?", ["My name is J.A.R.V.I.S, your personal assistant."]],
    [r"who created you ?", ["I was created by Tiago Setti using Python and NLTK."]],
    [r"what time is it(.*)", [get_time]],
    [r"(.*) date(.*)", [get_date]],
    [r"tell me a joke", [tell_joke]],
    [r"(.*) your location", ["I'm based in São Paulo, Brazil."]],
    [r"(.*) help(.*)", ["I can tell you the time, date, jokes, do calculations, and chat with you."]],
    [r"calculate (.*)", [lambda _, exp: calculate_expression(exp)]],
    [r"what is (.*)", ["%1 is something I'm still learning about."]],
    [r"why (.*)", ["Why do you think %1?"]],
    [r"quit", ["Goodbye! It was nice talking to you."]]
]

# Reflexões mais completas
my_reflections = {
    "i": "you",
    "i am": "you are",
    "i was": "you were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "me": "you"
}

# Função principal
def start_chat():
    print("J.A.R.V.I.S: Hello! Type 'quit' to exit.")
    chat = Chat(pairs, my_reflections)

    while True:
        user_input = input("> ")

        if user_input.lower() == "quit":
            print("Goodbye! It was nice talking to you.")
            break

        # Comandos especiais
        if "time" in user_input.lower():
            print(get_time())
            continue
        elif "date" in user_input.lower():
            print(get_date())
            continue
        elif "joke" in user_input.lower():
            print(tell_joke())
            continue
        elif user_input.lower().startswith("calculate"):
            expression = user_input[9:].strip()
            print(calculate_expression(expression))
            continue

        # Caso contrário, resposta do Chat normal
        print(chat.respond(user_input))


if __name__ == "__main__":
    start_chat()
