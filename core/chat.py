# J.A.R.V.I.S Chatbot Avançado
# Autor: Tiago Setti
# Bibliotecas necessárias: nltk

#instale o nltk se ainda não tiver: pip install nltk
#Primeira vez usando nltk.chat? Rode isso uma vez: import nltk  depois nltk.download('punkt')

from nltk.chat.util import Chat
from core.functions import get_time, get_date, tell_joke, calculate_expression

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

my_reflections = {
    "i": "you", "i am": "you are", "i was": "you were",
    "i'd": "you would", "i've": "you have", "i'll": "you will",
    "my": "your", "you are": "I am", "you were": "I was",
    "you've": "I have", "you'll": "I will", "your": "my",
    "yours": "mine", "me": "you"
}

chat = Chat(pairs, my_reflections)
