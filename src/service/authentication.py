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
from repository.users import get_user_by_email
from common.crypto import sha3_512_string, create_jwt
from common.config import config

import datetime


def login(email: str, password: str) -> str:
    user = get_user_by_email(email)

    if not user:
        return ""

    are_valid_credentials = user.password == sha3_512_string(password)

    if not are_valid_credentials:
        return ""

    payload = {
        "user_id": user.user_id,
        "email": user.email,
        # By Default, Sessions will expire in 48 hours
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=48),
        "role": user.role_name
    }

    return create_jwt(config.SECRET_KEY_JWT, payload)
