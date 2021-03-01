from flask import Flask, render_template, request
app = Flask(__name__)
import random
import time
import googlemaps

user_query = {"greetings": ["hi", "hello","hey","hlw","how you doing","what's up buddy","sup bitch"],
              "Coffee" : ["tell me how many types of coffee available ", "number of coffee available", "coffee?"]
}


bot_reply = {"greetings":["ola, how can I help you?", "hello, how can I help you?","hey, how can I help you?","hlw, how can I help you?","hey I am good thanks","hey just watching the world spin, how can I help you?"],
        "Coffee":[ "Affogato for 1.20$ \n, Americano for 3$ \n, Caffee Mocha for 2.50$ \n, Cappuchino for 1.50$ \n, Cold brew Coffee for 3.99$"],
        "default":["Sorry! I didn't catch that.Can you plz repeat that..?"]
        }
gmaps=googlemaps.Client(key="")
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


def intent_match(user_msg): 
    for intent, entity in user_query.items():
        if(user_msg.lower() in entity):
            return intent
    return "default"


def respond(user_msg):
    intent = intent_match(user_msg)
    return random.choice( bot_reply[intent] )   

def get_response(user_msg):
    bot_msg = ""
    #user_msg = ""
    while(1):
        if(user_msg == "get out"| "ok done"|"thank you"|"bye"|"later"):
            return "Bye. Nice to talk."
            break
        bot_msg = respond(user_msg)
        #time.sleep(5)
        return bot_msg
        



# ------------------------------------Flask App -------------------------------------

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/get')
def Chatbot():
    user_msg = request.args.get('msg')
    bot_reply  = str(get_response(user_msg))
    return bot_reply

if __name__=="__main__":
    app.run()
