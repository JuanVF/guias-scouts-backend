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

from service.material import get_document_in_route, add_new_material, remove_material
from service.material import ERROR_MESSAGE, ERROR_USER_TYPE_MISMATCH, ERROR_USER_DOES_NOT_EXISTS

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
            add_new_material(body.title, body.file, body.extension, decoded_token['email'])
            return get_response(200, {"message": "OK"})
    except Exception as e:
        return get_response(400, {"message": f"Invalid Body {e}"})
