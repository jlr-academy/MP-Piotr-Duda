import os
import pymysql
from dotenv import load_dotenv

def check_duplicates_two(rows, new_item):
    for row in rows:
        if new_item.upper() == row[1].upper():
            print(row[1])
            return True
    return False

def check_duplicates_in_db(new_item):

    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    # A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    # Add code here to insert a new record

    # Execute SQL query
    cursor.execute('SELECT product_id, name, price, in_stock FROM products')

    # Gets all rows from the result
    rows = cursor.fetchall()

    check_duplicates_two(rows, new_item)

    connection.commit()
    cursor.close()
    connection.close()

check_duplicates_in_db("Fanta")