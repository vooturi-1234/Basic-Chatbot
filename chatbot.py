from nltk.chat.util import Chat,reflections
pairs=[
       [r'hi',['hii']],
       [r'hii|hey|hello',['hi there']],
       [r'how are you',['i am fine hoping you good']],
       [r'what is your name',['my name is chatbot']],
       [r'sorry',['machine cannot have feelings its ok.']],
       [r'Thank you',['your welcome!']],
       [r'what  is python',['it is a programming language']],
       [r'What is your favorite color?',["I don't have any favorite color"]],
       [r'what is your age?',['I am ageless.']],
       [r'Tell me about weather condition?',["I don't know about te weather, but I can tal about anything!"]],
       [r'Where are you from?',['I live in the digital world']],
       [r'Can you help me?',['Of course! How can I assist you?']],
       [r'What did you do?',['I am here to chat with you any questions you have']],
       [r'Are you a robot?',['I am a chatbot powered by artificial intelligence']],
       [r'data means?',['data is a collection of information']],
       [r'Bye',['have a nice day!']],
]
chat=Chat(pairs,reflections)
def start_chat():
  print("WELCOME TO CHATBOT! HOW CAN I HELP YOU?")
  chat.converse()
if __name__=="__main__":
  start_chat()