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
import pymysql
from pymysql.err import MySQLError
from common.config import Config

config = Config()


class MySQLDatabase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.connection = None
            self.host_name = config.DB_HOST
            self.user_name = config.DB_USERNAME
            self.user_password = config.DB_PASSWORD
            self.db_name = config.DB_DATABASE
            self.initialized = True

    def connect(self):
        """Establece una conexión con la base de datos MySQL."""
        try:
            self.connection = pymysql.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.user_password,
                database=self.db_name
            )
            print("Connection to MySQL DB successful")
        except MySQLError as e:
            print(f"The error '{e}' occurred")

    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL dada con parámetros opcionales y realiza el commit de los cambios."""
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.connection.commit()
                print("Query executed successfully")
        except MySQLError as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query, params=None):
        """Ejecuta una consulta de lectura con parámetros opcionales y devuelve los datos obtenidos."""
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"The error '{e}' occurred")

    def close(self):
        """Cierra la conexión con la base de datos."""
        if self.connection:
            self.connection.close()
            print("MySQL connection is closed")


# Uso de la clase modificada
connection = MySQLDatabase()
connection.connect()
