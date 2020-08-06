import sqlite3

class DataBase:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, equation text, answer text)")
        self.conn.commit()

    def add_to_history(self, equation, answer):
        self.cur.execute("""INSERT INTO history VALUES (null, ?, ?)""", (equation, answer))
        self.conn.commit()

    def get_all(self):
        self.cur.execute("SELECT * FROM history")
        vals = self.cur.fetchall()
        return vals

    def __del__(self):
        self.conn.close()
