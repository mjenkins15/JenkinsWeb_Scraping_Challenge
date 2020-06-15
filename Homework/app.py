from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

#Create an instance of Flask
app = Flask (__name__)

#Use PyMongo to establish Mongo connection 
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#Route to render index.html template using data from Mongo
@app.route("/")
def index():

    #Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()

    #Return template and data
    return render_template("index.html", mars_data =  mars_dict)

#Route that will initiate the scrape function
@app.route("/scrape")
def scraper():

    #Run the scrape function
    mars_dict = mongo.db.mars_dict

    #mars_data = scrape_mars.scrape()
    mars_data = scrape()
    print(mars_data) 

    #Update the Mongo database and upsert_True
    mars_dict.update({}, mars_data, upsert = True)

    #Redirect back to the home page
    return redirect ("/", code = 302)

if __name__=="__main__":
    app.run(debug=True)
 

