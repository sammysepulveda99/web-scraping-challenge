#Importing dependencies
from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import os
import pymongo  

#Importing  our scraper into the app
import scraper_web_mars

#Setting our app with Flask
app = Flask(__name__)
mongo = PyMongo(app,uri ='mongodb://localhost:27017/mars')


@app.route("/")

def  index():
    data = mongo.db.collection.find.one()
    return render_template('index.html', mars=data)

@app.route("/scrape")

def mars_scrape():
    data_mars = scraper_web_mars.scrape()
    mongo.db.collection.update({},data_mars, upsert = True)
    return redirect("/")

if __name__ == "_main_":
    app.run(debug=True)