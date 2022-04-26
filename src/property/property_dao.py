from datetime import datetime
import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv()) # load from .env file
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

class PropertyDao:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
                        host=db_host,
                        database=db_name,
                        user=db_user,
                        password=db_password,
                        options="-c search_path=divit") # Heroku created this schema

    def insert(self, number_of_properties: int, created: datetime, region: str, created_by: str) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO property_for_sale_log (no_properties, created, region, created_by) VALUES (%s, %s, %s, %s)", [number_of_properties, created, region, created_by]);
            self.conn.commit()

    def __del__(self):
        if self.conn is not None:
            self.conn.close
