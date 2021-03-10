import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
import sys

class DB:
    def __init__(self):
        self._dbcon = None

    def __enter__(self):
        try:
            load_dotenv(find_dotenv())
            self._dbcon = psycopg2.connect(
                host=os.environ.get['AZ_POSTGRES_HOST'],
                user=os.environ.get['AZ_POSTGRES_USER'],
                password=os.environ.get['AZ_POSTGRES_PASSWORD'],
                database=os.environ.get['AZ_POSTGRES_DATABASE'],
                port=os.environ.get['AZ_POSTGRES_PORT']
            )
            self._cursor = self._dbcon.cursor()
            return self
        except:
            raise

    def __exit__(self, exc_type, exc_val, traceback):
        self._dbcon.close()

    def del_table(self):
        self._cursor.execute('DROP TABLE users IF EXISTS')
        self._dbcon.commit()

    def set_table(self):
        self._cursor.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL NOT NULL, names VARCHAR(100) NOT NULL)')
        self._dbcon.commit()

    def test_insert(self):
        self._cursor.execute("INSERT INTO users (names) VALUES ('Martin', 'Arthur');")
        self._dbcon.commit()

    def insert_user(self, name):
        query = 'INSERT INTO users (names) values (%s)'
        self._cursor.execute(query, name)
        self._dbcon.commit()

    def get_users(self):
        self._cursor.execute('SELECT * from users;')
        users = self._cursor.fetchall()
        users.sort()
        return users #jsonify sur le app.py

    def get_max(self):
        self._cursor.execute('SELECT MAX(id) from users;')
        max_id = self._cursor.fetchall()
        return max_id
