from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ✅ This is the primary key
    user_id = db.Column(db.String(50))
    bp = db.Column(db.String(20))
    sugar = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    advice = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ✅ Primary key for User too
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
