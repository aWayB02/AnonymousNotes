from psycopg_pool import ConnectionPool
from psycopg.errors import Error
from datetime import datetime
from uuid import uuid4
from dotenv import load_dotenv
import os

load_dotenv()


def create_pool(
        dbname: str, 
        user: str, password: str) -> ConnectionPool:
    """
    Функция для создания пула соединений
    """
    try:
        return ConnectionPool(conninfo=f"""dbname={dbname} user={user} 
                            password={password} port=5432 
                            host=localhost""", min_size=4, max_size=10)
    except Error as e:
        return e
    

class SecretNote:
    """
    Реализация класса для создание записки
    """
    def __init__(
                self, 
                url: uuid4, 
                password: bytes, 
                text: bytes, 
                date_remove: datetime
                ):
        
        self.url = url
        self.password = password
        self.text = text
        self.date_remove = date_remove
    
    def create_note(self):
        """
        Функция для создания записки
        """
        try:
            with pool.connection() as conn:
                conn.execute("""
                INSERT INTO notes(url, password, text, date_remove)
                VALUES(%s, %s, %s, %s)
                            """, (self.url, self.password, self.text, self.date_remove))
        except Error as e:
            return e


pool: ConnectionPool = create_pool(dbname=os.environ.get("DBNAME"), user=os.environ.get("USER"), password=os.environ.get("PASSWORD"))