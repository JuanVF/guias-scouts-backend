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
from service.users import create_user, get_user
from service.users import ERROR_MESSAGE, ERROR_PASSWORD_MISMATCH, ERROR_USER_DOES_NOT_EXISTS

from repository.users import DIRIGENTE_ROLE

from controller.user_model import ChangePasswordBody, RegisterUserBody


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
@extract_jwt_token()
def get_profile(decoded_token):
    """
    Get User Profile Endpoint, retrieves user information.
    ---
    tags:
      - user
    responses:
      200:
        description: Successful operation
        schema:
          type: object
          properties:
            user:
              type: object
              properties:
                fullname:
                  type: string
                email:
                  type: string
                birthday:
                  type: number
                  format: epoch_time
                patrol_name:
                  type: string
                role_name:
                  type: string
      404:
        description: User not found
      500:
        description: An error occurred while fetching user profile
    """
    try:
        current_user_id = decoded_token['user_id']

        user = get_user(current_user_id)

        if user == None:
            return get_response(404, {"message": "User not found"})

        return get_response(200, {"user": user})
    except Exception as e:
        return get_response(500, {"message": "An error occurred while fetching user profile"})


@user_blueprint.route("/register-user", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def register_user(decoded_token):
    """
    Register User Endpoint, creates a new user account.
    ---
    tags:
      - user
    parameters:
      - in: body
        name: user
        description: User to be registered
        required: true
        schema:
          type: object
          required:
            - fullname
            - email
            - password
            - birthday
            - id_patrol
            - id_role
          properties:
            fullname:
              type: string
            email:
              type: string
            password:
              type: string
            birthday:
              type: number
              format: epoch_time
            id_patrol:
              type: integer
            id_role:
              type: integer
    responses:
      200:
        description: User successfully registered
      400:
        description: Invalid request body
      401:
        description: Not enough privileges
      500:
        description: An error occurred while registering the user
    """
    # Only admins can create users
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        body = RegisterUserBody(**request.json)

        create_user(body.fullname, body.email, body.password,
                    body.birthday, body.id_patrol, body.id_role)

        return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})
