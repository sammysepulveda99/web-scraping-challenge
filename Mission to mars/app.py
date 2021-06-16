#Importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper_web_mars

#always run the scraper first on jupyter :(
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")


@app.route("/")
def index():
    mars = mongo.db.collection.find_one()
    if  mars == None or mars == {}:
        scrape()  
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars_data = scraper_web_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)