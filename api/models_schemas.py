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