from flask import Flask
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Password:</b> {my_password}"
    return html.format(
        name=os.getenv("NAME", "world"),
        my_password=os.getenv("PASSWORD", "Doh, you didn't set the password in the environment variable!")
    )
