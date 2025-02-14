from psycopg_pool import ConnectionPool
from psycopg.errors import Error


def create_pool(dbname, user, password) -> ConnectionPool:
    try:
        return ConnectionPool(conninfo=dbname, user=user, password=password)
    except Error as e:
        return e
    

class SecretNote:
    def __init__(self):
        pass