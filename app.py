from flask import Flask
app = Flask(__name__)

@app.route('/')
def user_page():
    return "您好啊"