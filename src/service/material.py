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

from repository.material import add_material, search_materials, Material, get_material_by_id, update_material_by_id
import base64
from common.mc import mc_handler
from common.time import current_timestamp
import os

ERROR_MESSAGE = "ERROR_MESSAGE"
SUCCESS_MESSAGE = "SUCCESS_MESSAGE"


def get_materials(q: str) -> list[dict]:
    """
    Service that can get all the materials and search in it
    """
    materials = search_materials(q)

    if len(materials) <= 0:
        return materials

    results = []

    for i in range(0, len(materials)):
        material = materials[i]

        results += [material.to_dict()]

    return results


def delete_material(id: str) -> str:
    """
    Service that can archive/delete a material
    """
    material = get_material_by_id(id)

    if material is None:
        return ERROR_MESSAGE

    material.active = 0

    result = update_material_by_id(material)

    if not result:
        return ERROR_MESSAGE

    return SUCCESS_MESSAGE


def add_new_material(title: str, file: str, extension: str, email: str):
    """
    Service that can add a new material
    """

    # Dividir la cadena por la coma y obtener la parte después de "base64"
    _, base64_encoded_data = file.split(',', 1)

    # Decodificar los datos base64
    decoded_data = base64.b64decode(base64_encoded_data)

    # Guardar los datos en un archivo

    # Nombre del archivo donde deseas guardar los datos
    file_name = title.replace(" ", "_") + "." + extension

    with open("media/"+file_name, "wb") as file:
        file.write(decoded_data)

    url = mc_handler.save_file(file_name)

    material = Material("", title, file_name, extension,
                        current_timestamp(), email, 1, url)

    if url is None:
        return ERROR_MESSAGE

    add_material(material)

    os.remove("media/"+file_name)

    return SUCCESS_MESSAGE
