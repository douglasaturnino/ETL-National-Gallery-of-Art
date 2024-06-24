import mysql.connector as mysql


class DatabaseConnection:
    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="user",
            passwd="password",
        )
        cls.connection = db_connection
