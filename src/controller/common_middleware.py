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
from functools import wraps
from flask import request

from common.response import get_response


def is_json_content_type():
    """
    Middleware to check if the body received is JSON type
    """
    def _is_json_content_type(f):
        @wraps(f)
        def __is_json_content_type(*args, **kwargs):
            content_type = request.headers.get('Content-Type')
            if content_type:
                media_type = content_type.split(
                    ';')[0].strip()  # Extract media type part
                if media_type != "application/json":
                    return get_response(400, 'Content-Type Not Supported!')
            else:
                return get_response(400, 'Content-Type Header Missing!')
            return f(*args, **kwargs)
        return __is_json_content_type
    return _is_json_content_type
