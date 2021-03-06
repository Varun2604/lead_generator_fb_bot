from app import db
from app.models import Subscribed_Users,Lead

def register_sender(sender_id):
    user = Subscribed_Users.query.filter_by(user_id=sender_id).first()
    if user is None:
        user = Subscribed_Users(user_id=sender_id)
        db.session.add(user)
        db.session.commit()

def register_lead_query(ai_response, event_response):
    if ai_response.get_intend() is not None:
        lead_query = Lead.query.filter_by(sender=event_response.get_sender_id(), entity=ai_response.get_intend()).first()
        if lead_query is None:
            lead = Lead(sender=event_response.get_sender_id(), entity=ai_response.get_intend())
            db.session.add(lead)
            db.session.commit()