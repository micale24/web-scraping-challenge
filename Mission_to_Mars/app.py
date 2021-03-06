from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars1

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")



# Route to render index.html template for initial scraping
@app.route("/")
def home():
    info = mongo.db.mars_db
    # Run the scrape function and save the results to a variable
    scraped_data = mission_to_mars1.scrapeMars()

    # Update the Mongo database using update and upsert=True
    info.update({}, scraped_data, upsert=True)

 # Find one record of data from the mongo database   
    info = mongo.db.mars_db.find_one()
    
    # Return template and data
    return render_template("./index.html", info=info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrapeMars():
    info = mongo.db.mars_db
    
    # Run the scrape function and save the results to a variable
    scraped_data = mission_to_mars1.scrapeMars()

    # Update the Mongo database using update and upsert=True
    info.update({}, scraped_data, upsert=True)

    # Redirect to the scraped data page
    return redirect("/",code=302)

   

if __name__ == "__main__":
    app.run(debug=True)