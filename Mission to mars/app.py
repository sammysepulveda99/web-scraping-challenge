#Importing dependencies
from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import os
import pymongo  

#Importing  our scraper into the app
import scraper_web_mars

#Setting our app with Flask
app = Flask(__name__, template_folder='template')
#Connecting to mongo
#app.config["MONGO_URI"]= "mongodb://localhost:27017/mars"
mongo = PyMongo(app,uri ="mongodb://localhost:27017/mars")
#mongo= PyMongo(app)


@app.route("/")
def  index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def mars_scrape():
    mars = mongo.db.mars
    mars_data = scraper_web_mars.scrape()
    mars.update({},mars_data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)