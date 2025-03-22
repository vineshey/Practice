from flask import Flask, jsonify
from flask_cors import CORS
from database import db, Hackathons  # Ensure 'Hackathons' is correctly imported from database
from scrap import h2skill, hackerEarth, dynamic, proElevate, devpost
from scrap_scholarships import fetch_filtered_links
from scrap_internships import fetch_internship_data
from scrap_internshala import fetch_course_data  # Fixed typo

import threading
import os

app = Flask(__name__)

CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)

# Create all tables in the database using app context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Hello! API is running."

# Route for fetching hackathons
@app.route('/get-hackathons')
def getHackathons():
    results = devpost()
    return jsonify(results)  # Ensure JSON response

# Route for fetching scholarships
@app.route('/get-scholarships')
def fetchScholarships():
    results = fetch_filtered_links()
    return jsonify(results)

# Route for fetching internships
@app.route('/get-internships')
def fetchInternships():
    results = fetch_internship_data()
    return jsonify(results)

# Route for fetching Internshala courses
@app.route('/get-internshala-courses')
def fetchInternshalaCourses():
    results = fetch_course_data()  # Fixed function name
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
