from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Set up mongo connection by flask_pymongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# Route to render index.html template using data from Mongo


@app.route("/")
def echo():
    final_mars_data = mongo.db.mars.find_one()
    return render_template("index.html", final_mars_data=final_mars_data)

# Route that will trigger the scrape function


@app.route("/scrape")
def scrapping_mars():
    final_mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update_one({}, {"$set": final_mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
