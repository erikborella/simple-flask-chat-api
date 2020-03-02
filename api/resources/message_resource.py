from flask_restful import Resource

from extensions import db

from models import Room, Message
from models_schemas import message_schema

from utils.validators import check_fields
from utils.auth import token_required

class Messages(Resource):

    def check_if_user_is_a_participant(self, user, room):
        
        for participant in room.participants:
            if user.id == participant.user.id:

                return True


    @token_required
    @check_fields(fields=('room_id', 'message'))
    def post(self, **kwargs):

        user = kwargs.get('user')

        fields = kwargs.get('fields')

        room_id = fields.get('room_id')
        message_text = fields.get('message')

        room = Room.query.filter_by(id=room_id).first_or_404("Room id cannot be find")

        if not self.check_if_user_is_a_participant(user, room):
            return { 'message': "you don't are a participant of this room" }, 403

        try:
            message = Message(message_text, user, room)

            print(message)

            db.session.add(message)
            db.session.commit()

            return {
                'message': "Message successfully send"
            }

        except:
            return {'message': 'Internal error'}, 500

        pass
