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
from common.db import connection


class Code:
    def __init__(self, code_id, code, user_id, user_name):
        self.code_id = code_id
        self.code = code
        self.user_id = user_id
        self.user_name = user_name


def get_latest_code_by_user_email(email: str):
    """
    Get the latest code generated by an user email
    """
    try:
        params = (email, )
        code_data = connection.execute_read_query("""SELECT 
                c.id AS code_id,
                c.code AS code,
                u.id AS user_id,
                u.fullname AS user_name
            FROM 
                `guias-scouts`.t_users_table u
            INNER JOIN 
                `guias-scouts`.t_codes_table c ON u.id = c.id_user
            INNER JOIN (
                SELECT 
                    id_user,
                    MAX(created_at) AS latest_created_at
                FROM 
                    `guias-scouts`.t_codes_table
                GROUP BY 
                    id_user
            ) AS max_dates ON c.id_user = max_dates.id_user AND c.created_at = max_dates.latest_created_at
            WHERE
                u.email = %s;""", params)

        if code_data and len(code_data) > 0:
            code = Code(*code_data[0])

            return code

        return None
    except:
        return None
