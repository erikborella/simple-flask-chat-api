from extensions import ma
from marshmallow import fields

""" Define all database Shemas to allow json serialissasion """

class UserSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    image = fields.String()

user_schema = UserSchema()
users_schemas = UserSchema(many=True)

class ParticipantSchema(ma.Schema):

    id = fields.Integer()
    user = fields.Nested(UserSchema)
    room_id = fields.Integer()

participant_schema = ParticipantSchema()
participants_schemas = ParticipantSchema(many=True)

class MessageSchema(ma.Schema):

    id = fields.Integer()
    message = fields.String()
    user = fields.Nested(UserSchema)

message_schema = MessageSchema()
messages_schemas = MessageSchema(many=True)

class RoomSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    participants = fields.List(fields.Nested(ParticipantSchema))
    messages = fields.List(fields.Nested(MessageSchema))


room_schema = RoomSchema()
rooms_schemas = RoomSchema(many=True)