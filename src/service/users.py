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
from common.crypto import sha3_512_string
from common.config import config

import datetime

ERROR_PASSWORD_MISMATCH = "ERROR_PASSWORD_MISMATCH"
ERROR_USER_DOES_NOT_EXISTS = "ERROR_USER_DOES_NOT_EXISTS"
ERROR_MESSAGE = "ERROR_MESSAGE"


def change_password(email: str, prevPassword: str, newPassword: str) -> str:
    """
    Service that can change the user password. Return empty string if everything is right
    """
    user = get_user_by_email(email)

    if not user:
        return ERROR_USER_DOES_NOT_EXISTS

    are_valid_credentials = user.password == sha3_512_string(prevPassword)

    if not are_valid_credentials:
        return ERROR_PASSWORD_MISMATCH

    user.password = sha3_512_string(newPassword)

    updated = update_user_by_id(user)

    if not updated:
        return ERROR_MESSAGE

    return ""
