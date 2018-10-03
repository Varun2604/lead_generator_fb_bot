from app import db

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, index=True, primary_key=True)
    email = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(120), index=True)
    entity = db.Column(db.String(120))

    def __repr__(self):
        return '<Lead {}>'.format(self.id)


class Scheduled_Push_Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10))
    message = db.Column(db.String(255))

    def __repr__(self):
        return '<Scheduled_Push_Message {}>'.format(self.id)

class Subscribed_Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)