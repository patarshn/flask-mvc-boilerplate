from flask import Blueprint
import controllers.UserController as UserController

UserBlueprint = Blueprint('UserBlueprint', __name__)
UserBlueprint.route('/', methods=['GET'])(UserController.index)
UserBlueprint.route('/create', methods=['POST'])(UserController.store)
UserBlueprint.route('/<int:user_id>', methods=['GET'])(UserController.show)