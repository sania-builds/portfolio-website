"""
models.py

Database models. The portfolio content itself is static (see data.py),
but messages people send through the contact form are real user data,
so they are stored in SQLite through this model.
"""

from datetime import datetime
from app import db


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ContactMessage {self.id} from {self.email}>"
