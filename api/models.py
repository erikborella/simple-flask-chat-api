from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    image = db.Column(db.String(500), nullable=True)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User: %r:%r>" % (self.name, self.email)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<Room: %r>" % self.name


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('participant', lazy=True))

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('participant', lazy=True))

    def __init__(self, user, room):
        self.user = user
        self.room = room

    def __repr__(self):
        return "<Participant: %r:%r>" % (self.user, self.room)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('message', lazy=True))

    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship('Room', backref=db.backref('message', lazy=True))

    def __init__(self, message, user, room):
        self.message = message

        self.user = user
        self.room = room

    def __repr__(self):
        return "<Message: %r:%r=%r>" % (self.user, self.room, self.message)