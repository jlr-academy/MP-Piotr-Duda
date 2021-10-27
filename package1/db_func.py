import os
import pymysql
from dotenv import load_dotenv

def sql_read(sql, data=None):
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
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

    return rows

def sql_execute(sql, data):
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
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    cursor.execute(sql, data)
    connection.commit()

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

def sql_execute_and_return_last_row_id(sql, data):
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
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    cursor.execute(sql, data)
    connection.commit()
    temp_id = cursor.lastrowid
    
    

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()
    
    return temp_id


def last_row_id():

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
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    customer_id = cursor.lastrowid

    connection.commit()

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

    return customer_id

