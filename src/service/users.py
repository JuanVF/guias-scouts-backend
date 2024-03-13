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

from repository.users import get_user_by_email, update_user_by_id, save_user, User, get_user_by_id
from repository.codes import insert_code_by_user_id
from common.crypto import sha3_512_string
from common.config import config
from common.time import current_timestamp
from common.text import generate_confirmation_code
from email.message import EmailMessage
import ssl
import smtplib

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


def get_user(user_id: str) -> dict:
    """
    Service that can get the user information by its id
    """
    user = get_user_by_id(user_id)

    if not user:
        return None

    if user.active == 0:
        return None

    return {
        "id": user_id,
        "fullname": user.fullname,
        "email": user.email,
        "birthday": user.birthday,
        "active": user.active,
        "created_at": user.created_at,
        "id_patrol": user.patrol_id,
        "id_role": user.role_id,
        "patrol_name": user.patrol_name,
        "role_name": user.role_name
    }


def send_confirmation_code(email_receiver, confirmation_code):

    email_sender = config.SENDER_EMAIL
    password = config.SENDER_EMAIL_PASSWORD

    subject = "Codigo de verificación - Guías Scouts"
    body = "Tu código de verificación es {}, no compartas este código con ninguna persona".format(
        confirmation_code)

    email = EmailMessage()
    email["From"] = email_sender
    email["To"] = email_receiver
    email["Subject"] = subject
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, email.as_string())


def create_user(fullname: str, email: str, password: str, birthday: str, id_patrol: int, id_role: int):
    """
    Create a new user and generate confirmation code.
    """
    try:
        # Generar un código de confirmación único
        confirmation_code = generate_confirmation_code()

        # Crear un objeto User con los datos proporcionados
        user = User(
            1, fullname, email, sha3_512_string(
                password), birthday, 0, current_timestamp(), id_patrol, id_role, "", ""
        )

        # Guardar el usuario en la base de datos
        user_id = save_user(user)

        if user_id == None:
            return ERROR_MESSAGE

        user.user_id = user_id

        succed_code_insert = insert_code_by_user_id(confirmation_code, user_id)

        if not succed_code_insert:
            return ERROR_MESSAGE

        send_confirmation_code(user.email, confirmation_code)

        return user
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir al crear el usuario
        print("Error creating user:", e)
        return None


def forgot_password(email: str):
    """
    Service that can change the user password by confirming a code in the user email. Return empty string if everything is right
    """
    user = get_user_by_email(email)

    if not user:
        return ERROR_USER_DOES_NOT_EXISTS

    confirmation_code = generate_confirmation_code()
    send_confirmation_code(user.email, confirmation_code)

    return user, confirmation_code
