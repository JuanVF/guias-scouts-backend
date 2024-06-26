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
from typing import List


class Material:
    def __init__(self, material_id, title, file_path, file_type, created_at, created_by, active, url):
        self.material_id = material_id
        self.title = title
        self.file_path = file_path
        self.file_type = file_type
        self.created_at = created_at
        self.created_by = created_by
        self.active = active
        self.url = url

    def to_dict(self) -> dict:
        return {
            "material_id": self.material_id,
            "title": self.title,
            "file_type": self.file_type,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "url": self.url
        }


def add_material(material: Material):
    """
    Save the material to the database.
    """
    try:

        params = (material.title, material.file_path, material.file_type, material.created_at, material.created_by,
                  material.active, material.url, )
        result = connection.execute_query("""INSERT INTO `guias-scouts`.t_materials_table
            (title, file_path, file_type, created_at, created_by, active, url)
                VALUES    
            (%s, %s, %s, %s, %s, %s, %s);
        
        """, params)
        return True

    except Exception as error:
        print("Error guardando material:", error)
        return False


def search_materials(q: str):
    """
    Search over the materials
    """
    try:
        materials = []

        # Ensure `q` is safely parameterized; `%s` is the placeholder for PyMySQL.
        query = """
        SELECT id, title, file_path, file_type, created_at, created_by, active, url
        FROM `guias-scouts`.t_materials_table
        WHERE title LIKE CONCAT('%%', COALESCE(NULLIF(%s,''), title), '%%')
        AND active = 1;
        """
        params = (q, )  # Tuple with a single value for the parameter in the query.

        materials_data = connection.execute_read_query(query, params)

        if materials_data and len(materials_data) > 0:
            for data in materials_data:
                materials.append(Material(*data))

        return materials
    except Exception as err:
        print(f"Error: {err}")
        return []


def get_material_by_id(id: str) -> Material:
    """
    Get a material by its id
    """
    try:
        params = (id, )
        material_data = connection.execute_read_query("""SELECT 
                                                                id, title, file_path, file_type, created_at, created_by, active, url
                                                            FROM `guias-scouts`.t_materials_table
                                                            WHERE id = %s;""", params)

        if material_data and len(material_data) > 0:
            return Material(*material_data[0])

        return None
    except:
        return []


def update_material_by_id(material: Material) -> bool:
    """
    Updates the material data by its id
    """
    try:
        params = (material.title, material.file_path,
                  material.file_type, material.active, material.url, material.material_id, )
        connection.execute_query("""UPDATE `guias-scouts`.t_materials_table
            SET title = %s,
                file_path = %s,
                file_type = %s, 
                active = %s,
                url = %s
            WHERE
                id = %s;""", params)

        return True
    except Exception as error:
        print("Error updating material: ", error)
        return False
