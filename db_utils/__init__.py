from app import db
from app.models import Subscribed_Users

def register_sender(sender_id):
    user = Subscribed_Users.query.filter_by(user_id=sender_id).first()
    if user is None:
        user = Subscribed_Users(user_id=sender_id)
        db.session.add(user)
        db.session.commit()

