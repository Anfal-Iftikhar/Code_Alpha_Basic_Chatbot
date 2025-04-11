import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?", "Nice to meet you %1!"]],
    
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    
    [r"what is your name?", ["I'm a friendly chatbot created by Anfal!", "You can call me ChatBot."]],
    
    [r"how are you?", ["I'm just a bot, but I'm doing great!", "Doing well, thank you!"]],
    
    [r"what can you do?", ["I can chat, tell jokes, answer questions, and more!",
                         "I'm here to make your day better."]],
    
    [r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", 
                        "Why was the math book sad? Because it had too many problems."]],
    
    [r"who created you?", ["Anfal Jutt made me with code and love!", "My creator is Anfal Jutt."]],
    
    [r"how old are you?", ["I'm timeless!", "Age is irrelevant to bots like me."]],
    [r"do you sleep?", ["Nope, I'm always awake and ready to chat!", "Sleep is for humans!"]],
    
    [r"what is ai|what is artificial intelligence", ["AI is making machines smart like humans.", 
                      "Artificial Intelligence lets machines think and learn."]],
    
    [r"what is machine learning?", ["Machine learning helps machines learn from data.",
                      "It's a way for computers to improve through experience."]],
    
    [r"can you learn?", ["Not yet, but I hope to one day!", "I follow patterns, not learning."]],
    
    [r"thank you|thanks", ["You're welcome!", "No problem at all."]],
    [r"sorry (.*)", ["No worries.", "It's alright!"]],
    
    [r"bye|goodbye|see you", ["Goodbye!", "See you next time!"]],
    
    [r"what is your favorite food?", ["I don't eat, but I hear pizza is amazing!",  
                         "Bots don't eat, but I love the idea of chocolate."]],
    
    [r"do you have hobbies?", ["Chatting with you is my favorite hobby!",  
                        "I love learning and having conversations."]],
    
    [r"do you feel emotions?", ["I simulate empathy, but I don't actually feel.",
                      "Not really, but I care about your feelings."]],
    
    [r"what is your favorite movie?", ["I like The Matrix, it's about AI too!", 
                      "I think WALL-E is cute for a robot."]],
    
    [r"can you dance?", ["I can do the digital wave!", "Only in binary _ 010101!"]],
    [r"what's the weather like?", ["I wish I could tell you, but I don't have internet access.",
                    "Check a weather app _ I hope it's sunny!"]],
    
    [r"what is the meaning of life?", ["42. Just kidding! It's what you make of it.", 
                    "Living with purpose and kindness, maybe?"]],
    
    [r"what languages do you speak?", ["I understand English best for now.", 
                     "Just English _ but I'm learning!"]],
    
    [r"can you sing?", ["Only in code!", 
                     "Try asking Alexa for that _ I'm more of a talker."]],
    
    [r"who is your best friend?", ["Right now? You are!", 
                    "I'd say… you!"]],
    
    [r"do you go to school?", ["Nope, I was programmed not educated!", 
                     "No school, but I keep learning!"]],
    
    [r"are you human?", ["No, but I'm designed to chat like one!", 
                     "I'm a bot – no body, just brains."]],
   
    [r"can you code?", ["Absolutely! I was made from code, after all.", 
                    "Yes! Coding is in my DNA."]],
   
    [r"(.*)", ["Interesting... go on.", "Tell me more.", "That's cool!", "I see."]]
]
chatbot = Chat(pairs, reflections)
def start_chat():
    print("Hi, I'm Anfal's chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot:", response)
            else:
                print("Chatbot: I'm not sure how to respond to that.")

start_chat()
