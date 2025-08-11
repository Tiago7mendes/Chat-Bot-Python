# Description: This is a chat bot program

from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|holla|hola|oi|eai)', ['hey there', 'hi there', 'haayyy', 'olá']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?', 'São Paulo, Brazil'],
    ['Who created you ?', ['Tiago Setti did using NLTK']],
    ['how is the weather in (.*) ?', ['the weather in %1 is amazing like always']],
    ['(.*) help(.*)', ['I can help you!']],
    ['(.*) your name ?', ['my name is J.A.R.V.I.S']]
]

my_dummy_reflections = {
    'go' : 'gone',
    'hello' : 'hey there'
}

chat = Chat(pairs, my_dummy_reflections)
#print(chat._substitute('go hello'))
chat.converse()