from flask import Flask
import os

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker on Heroku!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
