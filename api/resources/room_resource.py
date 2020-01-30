from flask_restful import Resource

from models import Room, Participant
from models_schemas import room_schema, participant_schema

from extensions import db

from utils.validators import check_fields
from utils.auth import token_required

class Rooms(Resource):

    @token_required
    @check_fields(fields=("name",))
    def post(self, **kwargs):

        user = kwargs.get('user')
        fields = kwargs.get('fields')

        name = fields.get('name')

        room = Room(name)
        participant = Participant(user, room)
        print(participant)

        try:
            db.session.add(room)
            db.session.add(participant)

            db.session.commit()

            return {
                'message': 'New room successfully created',
                'data': room_schema.dump(room)
            }, 201

        except:
            
            return {'message': 'Internal error'}, 500