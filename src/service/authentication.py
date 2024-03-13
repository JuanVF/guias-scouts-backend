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
from repository.users import get_user_by_email, update_user_by_id
from repository.codes import get_latest_code_by_user_email, get_all_codes
from common.crypto import sha3_512_string, create_jwt
from common.config import config

import datetime

CONFIRM_CODE_MESSAGE = "NEED_TO_CONFIRM"
ALREADY_ACTIVE = "ALREADY_ACTIVE"
ERROR_MESSAGE = "ERROR_MESSAGE"


def login(email: str, password: str) -> str:
    """
    Service that can do login. Will return the JWT Token for the user
    Will return empty string if error.
    If user is not yet activated will return "NEED_TO_CONFIRM"
    """
    user = get_user_by_email(email)

    if not user:
        return ""

    if user.active == 0:
        return CONFIRM_CODE_MESSAGE

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


def confirm_code(email: str, code: str) -> str:
    """
    Service that can do confirm an user. If everything is correct will return JWT.
    If already active will return "ALREADY_ACTIVE"
    else will return empty string
    """

    print("???")
    codes = get_all_codes()

    print(codes)

    user = get_user_by_email(email)

    if not user:
        return ""

    if user.active == 1:
        return ALREADY_ACTIVE

    code_data = get_latest_code_by_user_email(email)

    if not code_data:
        return ""

    is_valid_code = code == code_data.code

    if not is_valid_code:
        return ""

    user.active = 1

    updated = update_user_by_id(user)

    if not updated:
        return ERROR_MESSAGE

    payload = {
        "user_id": user.user_id,
        "email": user.email,
        # By Default, Sessions will expire in 48 hours
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=48),
        "role": user.role_name
    }

    return create_jwt(config.SECRET_KEY_JWT, payload)
