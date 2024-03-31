# Asegúrate de haber instalado PyMySQL en tu entorno.
# Puedes instalarlo ejecutando: pip install pymysql

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
