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

from controller.patrols_model import AddPatrol
from service.patrols import service_add_patrol

from common.response import get_response

from repository.users import DIRIGENTE_ROLE


patrol_blueprint = Blueprint('patrol', __name__, url_prefix='/patrol')


@patrol_blueprint.route("/add-patrol", methods=['POST'])
@is_json_content_type()
@extract_jwt_token()
def method_add_patrol(decoded_token):
    """
    Can add a new patrol
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
        body = AddPatrol(**request.json)

        result = service_add_patrol(body.name)

        if result != "":
            return get_response(500, {"message": "An error happened"})

        return get_response(200, {"message": "OK"})
    except:
        return get_response(400, {"message": "Invalid Body"})
