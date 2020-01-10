from extensions import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email')

user_schema = UserSchema()
users_schemas = UserSchema(many=True)