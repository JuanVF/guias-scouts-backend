# Copyright (c) 2024 Guias Scouts

# All rights reserved. This file and the source code it contains is
# confidential and proprietary to Guias Scouts. No part of this
# file may be reproduced, stored in a retrieval system, or transmitted
# in any form or by any means, electronic, mechanical, photocopying,
# recording, or otherwise, without the prior written permission of
# Guias Scouts.

# This file is provided "as is" with no warranties of any kind, express
# or implied, including but not limited to, any implied warranty of
# merchantability, fitness for a particular purpose, or non-infringement.
# In no event shall Guias Scouts be liable for any direct, indirect,
# incidental, special, exemplary, or consequential damages (including, but
# not limited to, procurement of substitute goods or services; loss of use,
# data, or profits; or business interruption) however caused and on any
# theory of liability, whether in contract, strict liability, or tort
# (including negligence or otherwise) arising in any way out of the use
# of this software, even if advised of the possibility of such damage.

# For licensing opportunities, please contact tropa92cr@gmail.com.
from flask import Blueprint, request
from controller.common_middleware import is_json_content_type
from controller.authorization_middleware import extract_jwt_token
from common.response import get_response
from service.users import change_password as service_change_password
from service.users import ERROR_MESSAGE, ERROR_PASSWORD_MISMATCH, ERROR_USER_DOES_NOT_EXISTS
from controller.user_model import ChangePasswordBody, RegisterUserBody
from flask_jwt_extended import jwt_required, get_jwt_identity
from repository.users import get_user_by_id
from service.users import create_user


user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route("/change-password", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def change_password(decoded_token):
    """
    Allows an user to change its password.
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: User's password data
        required: true
        schema:
          type: object
          required:
            - prevPassword
            - newPassword
          properties:
            prevPassword:
              type: string
              format: password
              example: your_old_password
            newPassword:
              type: string
              format: password
              example: your_new_password
    responses:
      200:
        description: Password Changed successfully
        schema:
          type: object
          properties:
            message:
              type: string
              description: Response Message
              example: OK
      400:
        description: Invalid Body
      401:
        description: Invalid Code
    """
    try:
        body = ChangePasswordBody(**request.json)

        result = service_change_password(
            decoded_token['email'], body.prevPassword, body.newPassword)

        if result == ERROR_USER_DOES_NOT_EXISTS:
            return get_response(400, {"message": "The user does not exists..."})

        if result == ERROR_PASSWORD_MISMATCH:
            return get_response(400, {"message": "The previous password does not match..."})

        if result == ERROR_MESSAGE:
            return get_response(400, {"message": "An error has ocurred, please try again..."})

        return get_response(200, {"message": "OK"})
    except:
        return get_response(400, {"message": "Invalid Body"})


@user_blueprint.route("/profile", methods=['GET'])
@jwt_required()
def get_profile():
    """
    Get User Profile Endpoint, retrieves user information.
    """
    try:
        # Obtener la identidad del usuario desde el token JWT
        current_user_id = get_jwt_identity()

        # Obtener la información del usuario desde la base de datos utilizando el correo electrónico
        user = get_user_by_id(current_user_id)

        if user:
            # Convertir el objeto User a un diccionario para serializarlo como JSON
            user_data = {
                "fullname": user.fullname,
                "email": user.email,
                "birthday": user.birthday,
                "patrol_name": user.patrol_name,
                "role_name": user.role_name
            }
            return get_response(200, {"user": user_data})
        else:
            return get_response(404, {"message": "User not found"})
    except Exception as e:
        return get_response(500, {"message": "An error occurred while fetching user profile"})


@user_blueprint.route("/register-user", methods=['POST'])
@is_json_content_type()
def register_user():
    try:
        body = RegisterUserBody(**request.json)

        create_user(body.fullname, body.email, body.password, body.birthday)

        return get_response(200, {"message": "OK"})
    except:
        return get_response(400, {"message": "Invalid Body"})
