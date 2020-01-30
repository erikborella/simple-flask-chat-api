from extensions import ma

""" Define all database Shemas to allow json serialissasion """

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'image')

user_schema = UserSchema()
users_schemas = UserSchema(many=True)

class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

room_schema = RoomSchema()
rooms_schemas = RoomSchema(many=True)

class ParticipantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'room_id')

participant_schema = ParticipantSchema()
participants_schemas = ParticipantSchema(many=True)

class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'message', 'user_id', 'room_id')

message_schema = MessageSchema()
messages_schemas = MessageSchema(many=True)