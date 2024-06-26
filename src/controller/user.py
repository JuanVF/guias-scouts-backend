# Copyright (c) 2024 Guias Scouts

# All rights reserved. This file and the media code it contains is
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

from service.users import change_password as service_change_password, reestablish_user_password_by_email, get_all_active_users, get_all_active_users_by_patrol, service_archive_user
from service.users import create_user, get_user, update_user
from service.users import ERROR_MESSAGE, ERROR_PASSWORD_MISMATCH, ERROR_USER_DOES_NOT_EXISTS

from repository.users import DIRIGENTE_ROLE

from controller.user_model import ChangePasswordBody, RegisterUserBody, UpdateUserBody


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


@user_blueprint.route("/get-all", methods=['GET'])
@extract_jwt_token()
def method_get_all_users(decoded_token):
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
    # Only admins can read all users
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        users = get_all_active_users()

        return get_response(200, {"users": users})
    except Exception as e:
        return get_response(500, {"message": "An error occurred while fetching user profile"})


@user_blueprint.route("/get-all-by-patrol", methods=['GET'])
@extract_jwt_token()
def method_get_all_users_by_patrol(decoded_token):
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
    # Only admins can read all users
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        patrol = request.args.get('patrol', None)

        users = get_all_active_users_by_patrol(patrol)

        return get_response(200, {"users": users})
    except Exception as e:
        return get_response(500, {"message": "An error occurred while fetching user patrols"})


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


@user_blueprint.route("/update-user", methods=['PUT'])
@is_json_content_type()
@extract_jwt_token()
def update_existing_user(decoded_token):
    """
    Register User Endpoint, updates an active user account.
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
            - id
            - fullname
            - email
            - password
            - birthday
            - id_patrol
            - id_role
          properties:
            id:
              type: number
            fullname:
              type: string
            email:
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

    try:
        body = UpdateUserBody(**request.json)

        # Only admins can edit other users
        if str(decoded_token['user_id']) != str(body.id) and decoded_token['role'] != DIRIGENTE_ROLE:
            return get_response(401, {"message": "Not enough privileges..."})

        updated = update_user(body.id, body.fullname, body.email,
                              body.birthday, body.id_patrol, body.id_role)

        if updated != "":
            raise Exception("user does not exists...")

        return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})


@user_blueprint.route("/reestablish-password", methods=['GET'])
@extract_jwt_token()
def reestablish_password(decoded_token):
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
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        email = request.args.get('email', None)

        result = reestablish_user_password_by_email(email)

        if result != "":
            raise Exception("ERROR")

        return get_response(200, {"message": "OK"})
    except Exception as e:
        print(e)
        return get_response(500, {"message": "An error ocurred while trying to reestablish the password"})


@user_blueprint.route("/delete-user", methods=['DELETE'])
@extract_jwt_token()
def method_archive_patrol(decoded_token):
    """
    Can delete a patrol by its name
    ---
    tags:
      - patrol
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
        user_id = request.args.get('id', None)

        result = service_archive_user(int(user_id))

        if result != "":
            return get_response(500, {"message": "An error happened"})

        return get_response(200, {"message": "OK"})
    except:
        return get_response(400, {"message": "Invalid Body"})
