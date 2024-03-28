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
from flask import Blueprint
from service.health import is_db_healthy
from common.response import get_response

health_blueprint = Blueprint('health', __name__, url_prefix='/health')


@health_blueprint.route("/db", methods=['GET'])
def health():
    """
    DB Health endpoint. Checks if DB connection is up and running.
    ---
    tags:
      - system_health
    responses:
      200:
        description: DB Health Status
      500:
        description: DB Is not healthy
    """
    is_healthy = is_db_healthy()

    data = {
        "message": "DB is not healthy..."
    }

    if (is_healthy):
        data['message'] = "DB is healthy!"

    return get_response(200, data)
