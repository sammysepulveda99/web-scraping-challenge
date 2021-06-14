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
mongo = PyMongo(app,uri ="mongodb://localhost:27017/mars")


@app.route("/")
def  index():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")

def mars_scrape():
    mars = scraper_web_mars.scrape()
    mongo.db.collection.update({},mars, upsert = True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)