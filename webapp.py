from flask import Flask, render_template, request
from web_chatbot import chat
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(chat.respond(userText))
    return str(chat.respond(userText))
 
 
if __name__ == "__main__":
    app.run()