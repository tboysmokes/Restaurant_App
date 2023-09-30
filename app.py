from dotenv import load_dotenv
from flask import Flask
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'newproject'

def get_data():
   url = 'https://api.yelp.com/v3/businesses/search'

   hearders = {
       'Authorization': f'Bearer {os.getenv("API_KEY")}'
   }

   params = {
       'term': 'restaurant',
       'location': 'lagos',
       'limit': 10
   }

   respond = requests.get(url, params=params, hearders=hearders)

   if respond.status_code == 200:
       data = respond.json()
   print(data)

   return data
 
if __name__ == '__main__':
    app.run(debug=True)