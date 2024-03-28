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

from repository.material import add_material, delete_material_by_id, Material
from repository.users import get_user_by_id, User
import base64
from common.mc import mc_handler
from common.time import current_timestamp
import os

ERROR_USER_TYPE_MISMATCH = "ERROR_USER_TYPE_MISMATCH"
ERROR_USER_DOES_NOT_EXISTS = "ERROR_USER_DOES_NOT_EXISTS"
ERROR_MESSAGE = "ERROR_MESSAGE"


def get_document_in_route(route: str) -> bytes:
    """
    Get the binary content of a document located at the specified route
    """
    try:
        with open(route, 'rb') as file:
            document_content = file.read()
        return document_content
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
        return None
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", e)
        return None


def add_new_material(title: str, file: str, extension: str, email: str):
    """
    Service that can add a new material
    """

    # El texto codificado en base64
    encoded_data = file

    # Dividir la cadena por la coma y obtener la parte después de "base64"
    _, base64_encoded_data = encoded_data.split(',', 1)

    # Decodificar los datos base64
    decoded_data = base64.b64decode(base64_encoded_data)

    # Guardar los datos en un archivo

    file_name = title.replace(" ", "_") + "." + extension  # Nombre del archivo donde deseas guardar los datos
    with open("media/"+file_name, "wb") as file:
        file.write(decoded_data)

    print("Los datos se han guardado correctamente en el archivo:", file_name)

    url = mc_handler.save_file(file_name)

    material = Material("", title, file_name, extension, current_timestamp(), email, 1, url)

    if url is None:
        return ERROR_MESSAGE
    else:
        add_material(material)
        os.remove("media/"+file_name)


        return True


def remove_material(material_id: int, user_id: int):
    """
    Service that remove a material document given its ID
    """

    user = get_user_by_id(user_id)

    if not user:
        return ERROR_USER_DOES_NOT_EXISTS

    if user.id_role != "dirigente" :
        return ERROR_USER_TYPE_MISMATCH

    deleted = delete_material_by_id(id)

    if not deleted:
        return ERROR_MESSAGE

    print("Material eliminado")
    return True

