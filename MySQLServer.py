#!/usr/bin/python3
import time
import mysql.connector
from mysql.connector import errorcode

def create_database(retries=3, delay=2):
    conn = None
    cursor = None
    attempt = 0
    while attempt < retries:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            return
        except mysql.connector.Error as err:
            attempt += 1
            if hasattr(err, "errno"):
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Access denied: check username/password and host permissions.")
                    break
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database error:", err)
                else:
                    print(f"MySQL Error [{getattr(err,'errno','n/a')}]: {err}")
            else:
                print(f"Connector error: {err}")
            if attempt < retries:
                print(f"Retrying ({attempt}/{retries}) in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Exceeded maximum retries.")
        finally:
            if cursor:
                try:
                    cursor.close()
                except Exception:
                    pass
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass

if __name__ == "__main__":
    create_database()
