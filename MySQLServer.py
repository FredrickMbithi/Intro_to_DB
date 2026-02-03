#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        cursor.close()
        db.close()

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
