from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hackathons(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    url = db.Column(db.String(50),nullable = False)
    location = db.Column(db.String(100),nullable = False)
    image = db.Column(db.String(50),nullable = False)
    time_left = db.Column(db.String(50),nullable = False)
    submissions = db.Column(db.String(50),nullable = False)
    prize_amount = db.Column(db.String(50),nullable = False)
    description = db.Column(db.Text,nullable = False)
    mode = db.Column(db.String(50),nullable = False)\
    
    def to_json(self):
        return {
        'id': self.id,
        'name': self.name,
        'url': self.url,
        'location': self.location,
        'image': self.image,
        'time_left': self.time_left,
        'submissions': self.submissions,
        'prize_amount': self.prize_amount,
        'description': self.description,
        'mode': self.mode
    }

