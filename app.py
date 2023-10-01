from dotenv import load_dotenv
from flask import Flask
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'newproject'

def get_data():
   
   # yelp API endpoint URL
   url = 'https://api.yelp.com/v3/businesses/search'

   # authorization header (API KEY)
   hearders = {
       'Authorization': f'Bearer {os.getenv("API_KEY")}'
   }

   # define search parameters
   params = {
       'term': 'restaurant',
       'location': 'lagos',
       'limit': 10
   }

   # send GET request to yelp API with the parameters
   respond = requests.get(url, params=params, hearders=hearders)

   #check if request was successful (status code 200)
   if respond.status_code == 200:
       data = respond.json()
   print(data)

   return data
 
if __name__ == '__main__':
    app.run(debug=True)