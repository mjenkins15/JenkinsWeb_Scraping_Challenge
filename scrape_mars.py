from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

#Create an instance of Flask
app = Flask (__name__)

#Use PyMongo to establish Mongo connection 
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
    def index():
        mars_dict = mongo.db.mars_dict.find)one()
        return render_template("index.html",
        mars_dict =  mars_dict)

@app.route("/scrape")
    def scraper():
        mars_dict = mongo.db.mars_dict
        mars_data = scrape_mars.scrape()
        mars_dict.update({}, mars)_data, upsert = True)
        return redirect ("/", code = 302)

if __name__=="__main__"
app.run(debug=True)
 

