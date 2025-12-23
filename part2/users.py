from flask_restx import Namespace, Resource, fields
from business.facade import HBnBFacade

api = Namespace("Users", description="User operations")
facade = HBnBFacade()

user_model = api.model("User", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "first_name": fields.String,
    "last_name": fields.String,
})

response_model = api.model("UserOut", {
    "id": fields.String,
    "email": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
})

@api.route("/")
class UserList(Resource):

    @api.marshal_list_with(response_model)
    def get(self):
        users = facade.list_users()
        return users

    @api.expect(user_model)
    @api.marshal_with(response_model)
    def post(self):
        data = api.payload
        user = facade.create_user(data)
        return user, 201


@api.route("/<string:user_id>")
class UserItem(Resource):

    @api.marshal_with(response_model)
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user

    @api.expect(user_model)
    @api.marshal_with(response_model)
    def put(self, user_id):
        updated = facade.update_user(user_id, api.payload)
        if not updated:
            api.abort(404, "User not found")
        return updated
