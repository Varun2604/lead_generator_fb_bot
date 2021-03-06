from app import db

class Lead(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    sender = db.Column(db.BigInteger, index=True, primary_key=True)
    email = db.Column(db.String(120), index=True)
    phone = db.Column(db.String(120), index=True)
    entity = db.Column(db.String(120))

    def __repr__(self):
        return '<Lead {}>'.format(self.id)


class Scheduled_Push_Message(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    day = db.Column(db.String(10), default="Sunday")
    message = db.Column(db.String(255))

    def __repr__(self):
        return '<Scheduled_Push_Message {}>'.format(self.id)

class Subscribed_Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, index=True, unique=True)