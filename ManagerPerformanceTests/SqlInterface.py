import sqlite3
import json


class Database:
    server = sqlite3.connect(':memory:')
    cursor = server.cursor()


class Auth(Database):
    table_name = 'auth'

    def __init__(self):
        self.setup_auth_table()

    def setup_auth_table(self):
        try:
            self.cursor.execute(f'''CREATE TABLE {self.table_name}
                           (
                           url TEXT KEY, 
                           type TEXT, 
                           token TEXT
                           )''')
            with open("config.json") as open_file:
                content = json.load(open_file)
                self.cursor.execute(f'''INSERT INTO {self.table_name} VALUES 
                ('{content["hostname"]}', 
                '{content["auth_type"]}', 
                '{content["auth"]}') ''')
        except sqlite3.OperationalError as e:
            pass

    def add_auth(self, url, auth_type, token) -> None:
        self.cursor.execute(f'''INSERT INTO {self.table_name} VALUES ('{url}', '{auth_type}', '{token}') ''')

    def get_all_auths(self) -> list:
        self.cursor.execute(f'''SELECT * FROM {self.table_name}''')
        return self.cursor.fetchall()

    def is_auth(self, url) -> bool:
        self.cursor.execute(f'''SELECT Count(*) FROM {self.table_name} where url = '{url}' ''')
        return self.cursor.fetchall()[0][0] > 0

    def get_auth_token(self, url) -> str:
        self.cursor.execute(f'''SELECT type, token FROM {self.table_name} where url = '{url}' ''')
        result = self.cursor.fetchone()
        return f'{result[0]} {result[1]}'

    def update_token(self, url, new_token) -> None:
        self.cursor.execute(f'''UPDATE {self.table_name} SET token = '{new_token}' WHERE url = '{url}' ''')

    def delete_token(self, url) -> None:
        self.cursor.execute(f'''DELETE FROM {self.table_name} where url = '{url}' ''')

    def get_auth_by_row_id(self, row_id):
        self.cursor.execute(f'''SELECT * FROM {self.table_name} where rowId = '{row_id}' ''')
        return self.cursor.fetchall()[0]

