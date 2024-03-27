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


class Material:
    def __init__(self, material_id, title, document, route):
        self.material_id = material_id
        self.title = title
        self.document = document


def add_material(material: Material):
    """
    Save the material to the database.
    """
    try:
        params = (material.title, material.document, material.route,)
        result = connection.execute_query("""INSERT INTO t_material_table
            (title, document)
            VALUES (%s, %s);""", params)

        print("Material guardado")

        return True
    except Exception as error:
        print("Error guardando material:", error)
        return False


def delete_material_by_id(material_id: int):
    """
    Delete material by its ID
    """
    try:
        params = (material_id,)
        result = connection.execute_query("""
                    DELETE FROM t_material_table
                    WHERE id = %s;
                """, params)

        print("Material eliminado correctamente.")
        return True
    except Exception as error:
        print("Error al eliminar material:", error)
        return False
