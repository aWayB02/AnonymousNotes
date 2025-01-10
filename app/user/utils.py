from db import db_connect
from datetime import datetime

def delete_notes():
    conn = db_connect()
    cur = conn.cursor()
    time = datetime.now()
    cur.execute("DELETE FROM notes WHERE timer <= %s;", (time, ))
    conn.commit()
    conn.close()