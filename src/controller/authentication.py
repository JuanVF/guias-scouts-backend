from flask import Blueprint, request
from controller.common_middleware import is_json_content_type
from controller.authentication_model import LoginBody
from flasgger import swag_from

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
    body = LoginBody(**request.json)

    print(body.email)
    print(body.password)

    return "Authentication Page"
