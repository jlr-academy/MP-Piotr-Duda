import pymysql
from dotenv import load_dotenv
import os

def add_item_to_db():
    # Load environment variables from .env file
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
    name=input("Enter name: ")

    is_duplicate = check_duplicates_in_db(name, cursor)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        price=float(input("Enter price: "))
        in_stock=float(input("Enter number of items in stock: "))

        sql = "INSERT INTO products (name, price, in_stock) VALUES (%s, %s, %s)"
        val = (name, price, in_stock)
        cursor.execute(sql, val)

    

def check_duplicates_in_db(new_item, cursor):

    # Execute SQL query
    cursor.execute('SELECT name FROM products')

    # Gets all rows from the result
    rows = cursor.fetchall()

    for row in rows:
        if new_item.upper() == row[0].upper():
            print(row[0])
            return True
    return False

add_item_to_db()


