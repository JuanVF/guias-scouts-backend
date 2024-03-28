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
import jwt

from functools import wraps
from flask import request

from common.response import get_response
from common.config import config


def extract_jwt_token():
    """
    Middleware to extract JWT token from Authorization header
    """
    def _extract_jwt_token(f):
        @wraps(f)
        def __extract_jwt_token(*args, **kwargs):
            # Extract Bearer token from Authorization header
            auth_header = request.headers.get('Authorization')

            if not auth_header or not auth_header.startswith('Bearer '):
                return get_response(401, {"message": "Invalid Authorization header!"})

            token = auth_header.split(' ')[1]

            try:
                # Decode JWT token
                decoded_token = jwt.decode(
                    token, config.SECRET_KEY_JWT, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return get_response(401, {"message": "Token expired!"})
            except jwt.InvalidTokenError:
                return get_response(401, {"message": "Invalid token!"})

            # Pass decoded token to the endpoint function
            return f(decoded_token, *args, **kwargs)
        return __extract_jwt_token
    return _extract_jwt_token
