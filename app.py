from flask import Flask
from flask_cors import CORS
from database import db,Hackathons  # Ensure 'Hackathons' is correctly imported from database
from scrap import h2skill, hackerEarth, dynamic, proElevate, devpost
import threading
import os

app = Flask(__name__)

CORS(app)

# Corrected typo in the configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrected typo here

db.init_app(app)

# Create all tables in the database using app context
with app.app_context():
    db.create_all()
    #db.drop_all()

@app.route('/')
def home():
    return "hello"

@app.route('/fetch-hackathons')
def fetchHackathons():
    # Use app context for database-related actions within threads
    def run_scraping():
        with app.app_context():
            devpost()
            h2skill()
            hackerEarth()
            dynamic()
            proElevate()
            
    
    # Start the scraping tasks in separate threads
    threads = []
    for target_function in [devpost,h2skill,
            hackerEarth,
            dynamic,
            proElevate]:
        thread = threading.Thread(target=run_scraping)
        thread.start()
        threads.append(thread)

    # Don't block the main thread by waiting for them to finish
    for thread in threads:
        thread.join()  # If you want to wait for all threads to finish before continuing (optional)

    return 'Scraping Initiated! Data is being processed in the background.'

@app.route('/get-hackathons')
def getHackathons():
    results = Hackathons.query.all()
    results = [result.to_json() for result in results]
    
    return results
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
