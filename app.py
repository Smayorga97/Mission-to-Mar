#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies & tools
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping


# In[2]:


# Set up Flask
app = Flask(__name__)


# In[3]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[4]:


# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[5]:



# Define next route
@app.route("/scrape")
def scrape():
    print("start_scrape")
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    print("end_scrape")
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


# In[ ]:


# Tell Flask to run
if __name__ == "__main__":
    app.run()


# In[ ]:




