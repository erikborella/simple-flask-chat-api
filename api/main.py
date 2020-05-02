from app_creator import create_app
from flask_restful import Api

from flask import send_from_directory

from resources.user_resource import Users, GetOneUser, GetAllUsers, Image
from resources.auth_resource import Auth, Logout
from resources.room_resource import Rooms, GetOneRoom, GetAllRooms, EnterRoom, \
                                    GetParticipatingRooms, LeaveRoom

from resources.message_resource import Messages, GetMessages


app = create_app()
api = Api(app)

api.add_resource(Users, '/api/user')
api.add_resource(GetOneUser, '/api/user/<user_id>')
api.add_resource(Image, '/api/user/image')
api.add_resource(GetAllUsers, '/api/users')

api.add_resource(Auth, '/api/auth')
api.add_resource(Logout, '/api/auth/logout')

api.add_resource(Rooms, '/api/room')
api.add_resource(GetOneRoom, '/api/room/<room_id>')
api.add_resource(GetAllRooms, '/api/rooms')
api.add_resource(GetParticipatingRooms, '/api/rooms/participating')

api.add_resource(EnterRoom, '/api/room/enter')
api.add_resource(LeaveRoom, '/api/room/leave/<room_id>')

api.add_resource(Messages, '/api/message')
api.add_resource(GetMessages, '/api/message/<room_id>')




if __name__ == "__main__":
    app.run()