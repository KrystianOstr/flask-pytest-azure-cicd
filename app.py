from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps!"

@app.route('/janusz')
def hello_janusz():
    return "Hello, Janusz!"

def add(a,b):
    return a+b



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)