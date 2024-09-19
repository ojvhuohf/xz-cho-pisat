import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    db_name: str

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def init_table(self):
        self.open()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, 
                            name STRING(100), specialty STRING(200), qualifications STRING(200), img TEXT)''')
        self.close()
    
    def add_data(self, info):
        print(info)
        self.open()
        self.cursor.execute('''INSERT INTO user (name, specialty, qualifications, img) 
                            VALUES (?, ?, ?, ?)''', info)
        self.conn.commit()
        self.close()

    def get_data(self):
        self.open()
        self.cursor.execute('''SELECT * FROM user''')
        data = self.cursor.fetchall()
        return data
        

db = DB_Controller('main.db')
db.init_table()