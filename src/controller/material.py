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

from service.material import get_materials, add_new_material
from service.material import ERROR_MESSAGE

from repository.users import DIRIGENTE_ROLE

from controller.material_model import CreateMaterialModel

material_blueprint = Blueprint('material', __name__, url_prefix='/material')


@material_blueprint.route("/add-material", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def add_material(decoded_token):
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})
    try:
        body = CreateMaterialModel(**request.json)
        if body.extension != "pdf":
            return get_response(401, {"message": "Not a pdf document..."})
        else:
            add_new_material(body.title, body.file,
                             body.extension, decoded_token['email'])
            return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})


@material_blueprint.route("/search", methods=['GET'])
@extract_jwt_token()
def change_password(token_payload):
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
        q = request.args.get('q', '')

        materials = get_materials(q)

        return get_response(200, {"message": "OK", "materials": materials})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})
