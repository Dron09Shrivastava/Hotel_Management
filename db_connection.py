import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="dronmysql@09",
        database="hotel_db"
        )
