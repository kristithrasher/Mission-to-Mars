# Import dependencies/tools
# Use Flask to render a template, redirecting to another URL and creating a URL
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact with out Mongo daabase
from flask_pymongo import PyMongo
# Use the scraping code and convert from Jupyter to Python
import scraping

# Set Up Flask for web app
app = Flask(__name__)

# tell Python how to connect to Mongo using PyMongo. use flask_pymongo to set up mongo connection
# The URI we will be using to connect to our app Mongo. It is saying that the app can reach Mongo
# through our localhost server using port 27017, using database named mars_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up App Routes
# Main one for everyone can view
@app.route("/")
def index():
        mars = mongo.db.mars.find_one() 
        return render_template("index.html", mars=mars) 

# set up our scraping route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

# Tell Flask to run 
if __name__ == "__main__":
   app.run()






