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

DIRIGENTE_ROLE = 'dirigente'
PROTAGONISTA_ROLE = 'protagonista'


class User:
    def __init__(self, user_id, fullname, email, password, birthday, active, created_at, patrol_id, role_id, patrol_name, role_name):
        self.user_id = user_id
        self.fullname = fullname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.active = active
        self.created_at = created_at
        self.patrol_id = patrol_id
        self.role_id = role_id
        self.patrol_name = patrol_name
        self.role_name = role_name

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "fullname": self.fullname,
            "email": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "active": self.active,
            "created_at": self.created_at,
            "patrol_id": self.patrol_id,
            "role_id": self.role_id,
            "patrol_name": self.patrol_name,
            "role_name": self.role_name
        }


def get_all_users():
    """
    Returns all the active users
    """
    try:
        results = []
        users_data = connection.execute_read_query("""SELECT 
                u.id AS user_id,
                u.fullname AS user_fullname,
                u.email AS user_email,
                u.password AS user_password,
                u.birthday AS user_birthday,
                u.active AS user_active,
                u.created_at AS user_created_at,
                u.id_patrol AS patrol_id,
                u.id_role AS id_role,
                p.name AS patrol_name,
                r.name AS role_name
            FROM 
                `guias-scouts`.t_users_table u
            LEFT JOIN 
                `guias-scouts`.t_patrols_table p ON u.id_patrol = p.id
            INNER JOIN 
                `guias-scouts`.t_roles_table r ON u.id_role = r.id
            WHERE
                u.active = 1;""", None)

        if users_data and len(users_data) > 0:
            for data in users_data:
                results.append(User(*data).to_dict())

        return results
    except Exception as e:
        print(f"get_all_users error: {e}")
        return []


def get_all_users_by_patrol(patrol: str):
    """
    Returns all the users by its patrol group
    """
    try:
        params = (patrol, )
        results = []
        users_data = connection.execute_read_query("""SELECT 
                u.id AS user_id,
                u.fullname AS user_fullname,
                u.email AS user_email,
                u.password AS user_password,
                u.birthday AS user_birthday,
                u.active AS user_active,
                u.created_at AS user_created_at,
                u.id_patrol AS patrol_id,
                u.id_role AS id_role,
                p.name AS patrol_name,
                r.name AS role_name
            FROM 
                `guias-scouts`.t_users_table u
            LEFT JOIN 
                `guias-scouts`.t_patrols_table p ON u.id_patrol = p.id
            INNER JOIN 
                `guias-scouts`.t_roles_table r ON u.id_role = r.id
            WHERE
                u.active = 1 AND p.name = %s;""", params)

        if users_data and len(users_data) > 0:
            for data in users_data:
                results.append(User(*data).to_dict())

        return results
    except Exception as e:
        print(f"get_all_users_by_patrol error: {e}")
        return []


def get_user_by_email(email: str):
    """
    Query an user by its email
    """
    try:
        params = (email, )
        user_data = connection.execute_read_query("""SELECT 
                u.id AS user_id,
                u.fullname AS user_fullname,
                u.email AS user_email,
                u.password AS user_password,
                u.birthday AS user_birthday,
                u.active AS user_active,
                u.created_at AS user_created_at,
                u.id_patrol AS patrol_id,
                u.id_role AS id_role,
                p.name AS patrol_name,
                r.name AS role_name
            FROM 
                `guias-scouts`.t_users_table u
            LEFT JOIN 
                `guias-scouts`.t_patrols_table p ON u.id_patrol = p.id
            INNER JOIN 
                `guias-scouts`.t_roles_table r ON u.id_role = r.id
            WHERE
                u.email = %s;""", params)

        if user_data and len(user_data) > 0:
            user = User(*user_data[0])

            return user

        return None
    except:
        return None


def get_user_by_id(user_id: int):
    """
    Query a user by its ID
    """
    try:
        params = (user_id, )

        user_data = connection.execute_read_query("""SELECT 
                u.id AS user_id,
                u.fullname AS user_fullname,
                u.email AS user_email,
                u.password AS user_password,
                u.birthday AS user_birthday,
                u.active AS user_active,
                u.created_at AS user_created_at,
                u.id_patrol AS patrol_id,
                u.id_role AS id_role,
                p.name AS patrol_name,
                r.name AS role_name
            FROM 
                `guias-scouts`.t_users_table u
            LEFT JOIN 
                `guias-scouts`.t_patrols_table p ON u.id_patrol = p.id
            INNER JOIN 
                `guias-scouts`.t_roles_table r ON u.id_role = r.id
            WHERE
                u.id = %s;""", params)

        if user_data and len(user_data) > 0:
            user = User(*user_data[0])

            return user

        return None
    except:
        return None


def update_user_by_id(user: User) -> bool:
    """
    Updates the user data by its id
    """
    try:
        params = (user.fullname, user.patrol_id, user.email,
                  user.birthday, user.password, user.active, user.role_id, user.user_id,)
        result = connection.execute_query("""UPDATE `guias-scouts`.t_users_table
            SET fullname = %s,
                id_patrol = %s,
                email = %s,
                birthday = %s, 
                password = %s,
                active = %s,
                id_role = %s
            WHERE
                id = %s;""", params)

        return True
    except Exception as error:
        print("Error updating user: ", error)
        return False


def save_user(user: User) -> Optional[int]:
    """
    Save the user to the database and return the user ID.
    """
    try:
        params = (user.fullname, user.email, user.password, user.birthday,
                  user.active, user.role_id, user.patrol_id, user.created_at, )

        connection.execute_query("""INSERT INTO `guias-scouts`.t_users_table
            (fullname, email, password, birthday, active, id_role, id_patrol, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""", params)

        result = connection.execute_read_query(
            """SELECT LAST_INSERT_ID() as user_id;""")

        # After insertion, retrieve the ID of the newly inserted user
        if result and len(result) > 0:
            return result[0][0]

        return None
    except Exception as error:
        print("Error saving user:", error)
        return None
