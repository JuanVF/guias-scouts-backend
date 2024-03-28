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

from service.material import get_materials, add_new_material, delete_material
from service.material import ERROR_MESSAGE, SUCCESS_MESSAGE

from repository.users import DIRIGENTE_ROLE

from controller.material_model import CreateMaterialModel

material_blueprint = Blueprint('material', __name__, url_prefix='/material')


@material_blueprint.route("/add-material", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def add_material(decoded_token):
    """
    Allows an user to upload a material
    ---
    tags:
      - material
    summary: Adds a new material
    description: |
      Allows users with DIRIGENTE_ROLE to add new materials to the system. Only PDF documents are accepted.
    consumes:
      - application/json
    produces:
      - application/json
    security:
      - jwt: []
    parameters:
      - in: body
        name: body
        description: Material data
        required: true
        schema:
          type: object
          required:
            - title
            - file
            - extension
          properties:
            title:
              type: string
              format: text
              example: A Material Title
            file:
              type: string
              format: base64
              example: data:text/plain;base64,SG9sYSBNdW5kbyE=
            extension:
              type: string
              format: text
              example: pdf
    responses:
      200:
        description: Material added successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: OK
      401:
        description: Unauthorized - Not enough privileges or not a PDF document
        schema:
          type: object
          properties:
            message:
              type: string
              example: Not enough privileges...
      400:
        description: Bad Request - Invalid body data
        schema:
          type: object
          properties:
            message:
              type: string
              example: Invalid Body {error details}
    """
    if decoded_token['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": "Not enough privileges..."})
    try:
        body = CreateMaterialModel(**request.json)
        if body.extension != "pdf":
            return get_response(401, {"message": "Not a pdf document..."})
        else:
            result = add_new_material(body.title, body.file,
                                      body.extension, decoded_token['email'])

            if result == ERROR_MESSAGE:
                return get_response(500, {"message": f"An error happened. Please try again..."})

            return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})


@material_blueprint.route("/search", methods=['GET'])
@extract_jwt_token()
def search_materials(token_payload):
    """
    Allows an user to search materials
    ---
    tags:
      - material
    parameters:
      - in: path
        name: q
        required: false
        schema:
          type: string
        description: The value you are searching. Empty for all results
    responses:
      200:
        description: Successful operation
        schema:
          type: object
          properties:
            message:
              type: string
            materials:
              type: array
              items:
                type: object
                properties:
                  created_at:
                    type: string
                  created_by:
                    type: string
                  file_type:
                    type: string
                  material_id:
                    type: number
                  title:
                    type: string
                  url:
                    type: string
                    format: url
      401:
        description: unauthorized
      500:
        description: An error occurred while fetching materials
    """
    try:
        q = request.args.get('q', '')

        materials = get_materials(q)

        return get_response(200, {"message": "OK", "materials": materials})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})


@material_blueprint.route("/delete", methods=['DELETE'])
@extract_jwt_token()
def archive_material(token_payload):
    """
    Allows an user to delete a material
    ---
    tags:
      - material
    parameters:
      - in: path
        name: id
        required: true
        schema:
          type: string
        description: The id of the material to delete
    responses:
      200:
        description: Successful operation
        schema:
          type: object
          properties:
            message:
              type: string
      401:
        description: unauthorized
      500:
        description: An error occurred while fetching materials
    """
    if token_payload['role'] != DIRIGENTE_ROLE:
        return get_response(401, {"message": f"Unauthorized!"})

    try:
        id = request.args.get('id', None)

        if id is None:
            raise Exception("id can not be null...")

        result = delete_material(id)

        if result == ERROR_MESSAGE:
            return get_response(500, {"message": f"An error happened. Please try again..."})

        return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})
