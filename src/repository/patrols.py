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
from common.db import connection
from typing import Optional


class Patrol:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }


def add_patrol(name: str) -> Optional[int]:
    """
    Saves a new patrol group
    """
    try:
        params = (name, )

        connection.execute_query("""INSERT INTO `guias-scouts`.t_patrols_table
            (name)
            VALUES (%s);""", params)

        result = connection.execute_read_query(
            """SELECT LAST_INSERT_ID() as patrol_id;""")

        # After insertion, retrieve the ID of the newly inserted user
        if result and len(result) > 0:
            return result[0][0]

        return None
    except Exception as error:
        print("Error saving user:", error)
        return None
