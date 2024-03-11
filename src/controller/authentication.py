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
from controller.authentication_model import LoginBody
from common.response import get_response
from service.authentication import login as service_login

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route("/login", methods=['POST'])
@is_json_content_type()
def login():
    """
    Login Endpoint, returns a JWT if correct credentials.
    ---
    tags:
      - Authentication
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        description: User's login credentials
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              format: email
              example: user@example.com
            password:
              type: string
              format: password
              example: yourpassword
    responses:
      200:
        description: Authentication successful
        schema:
          type: object
          properties:
            token:
              type: string
              description: JWT token
              example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwicm9sZSI6IkRpcmlnZW50ZSIsImlhdCI6MTUxNjIzOTAyMn0.uK8RGsp5ZgdFl-cnZDKPd8y768Ceas3l3aogtEC07uk
      401:
        description: Authentication failed
    """
    try:
        body = LoginBody(**request.json)

        token = service_login(body.email, body.password)

        if token == "":
            # This message is in purpose. An attacker might be trying to bruteforce users to find existing users
            # They won't know if we sent Invalid Credentials always
            return get_response(400, {"message": "Invalid Credentials..."})

        return get_response(200, {"message": "OK", "token": token})
    except:
        return get_response(400, {"message": "Invalid Body"})
