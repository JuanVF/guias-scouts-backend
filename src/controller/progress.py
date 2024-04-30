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

from service.progress import get_all_progress_types, get_questions_by_progress_type_and_user_id, evaluate_form

from repository.users import DIRIGENTE_ROLE
from controller.progress_model import Questions

progress_blueprint = Blueprint('progress', __name__, url_prefix='/progress')


@progress_blueprint.route("/all_progress_types", methods=['GET'])
@is_json_content_type()
@extract_jwt_token()
def get_get_all_progress_types(decoded_token):
    """
    Allows an user to request all the progress types
    ---
    tags:
      - user
    consumes:
      - application/json
    responses:
      200:
        description: Return all progress types
        schema:
          type: object
          properties:
            message:
              type: string
              description: Response Message
              example: OK
      400:
        description: Invalid Body
    """
    try:
        result = get_all_progress_types()

        return get_response(200, {"message": "OK", "types": result})
    except Exception as error:
        print(error)
        return get_response(400, {"message": "Invalid Body"})


@progress_blueprint.route("/questions", methods=['GET'])
@is_json_content_type()
@extract_jwt_token()
def get_filter_questions(decoded_token):
    """
    Allows an user to request all the progress types
    ---
    tags:
      - user
    consumes:
      - application/json
    responses:
      200:
        description: Return all progress types
        schema:
          type: object
          properties:
            message:
              type: string
              description: Response Message
              example: OK
      400:
        description: Invalid Body
    """
    # Only admins can read other user forms
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        progress_type = request.args.get('progressType', None)
        user_id = request.args.get('userId', None)

        if progress_type == None or user_id == None:
            raise Exception("progressType or userId are required parameters")

        result = get_questions_by_progress_type_and_user_id(
            progress_type, user_id)

        return get_response(200, {"message": "OK", "questions": result})
    except Exception as error:
        print(error)
        return get_response(400, {"message": "Invalid Body"})


@progress_blueprint.route("/evaluate", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def method_evaluate_form(decoded_token):
    """
    Allows an user to request all the progress types
    ---
    tags:
      - user
    consumes:
      - application/json
    responses:
      200:
        description: Return all progress types
        schema:
          type: object
          properties:
            message:
              type: string
              description: Response Message
              example: OK
      400:
        description: Invalid Body
    """
    # Only admins can read other user forms
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})

    try:
        body = Questions(**request.json)

        if len(body.questions) <= 0:
            raise Exception("at least one question is required")

        result = evaluate_form(body.questions, body.user_id)

        return get_response(200, {"message": "OK", "body": result})
    except Exception as error:
        print(error)
        return get_response(400, {"message": "Invalid Body"})
