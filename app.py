from dotenv import load_dotenv
from flask import Flask
import requests
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'newproject'


if __name__ == '__main__':
    app.run(debug=True)