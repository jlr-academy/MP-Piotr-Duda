import os
import pymysql
from dotenv import load_dotenv
from package1.sql_queries import GET_COURIER_QUERY, GET_PRODUCTS_QUERY

def get_db_connection():
    
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
        )
    return connection

def print_courier_db(): 

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(GET_COURIER_QUERY)

    # Gets all rows from the result
    rows = cursor.fetchall()
    for row in rows:
        print(f'courier_id: {row[0]}, courier: {row[1]}, phone: {row[2]}')

    connection.commit()
    cursor.close()
    connection.close()

def print_product_db(): 

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(GET_PRODUCTS_QUERY)

    # Gets all rows from the result
    rows = cursor.fetchall()
    for row in rows:
        print(f'product_id: {row[0]}, product: {row[1]}, price: {row[2]}, quantity: {row[3]}')

    connection.commit()
    cursor.close()
    connection.close()

def add_product_index_to_list():
    items_list = []
    while True:
        try:
            choice = int(input("Do you want add products to the order? 0 - No / 1 - Yes"))
            if choice == 0:
                os.system("cls")
                return items_list
                #break
            elif choice == 1:
                print_product_db()
                connection = get_db_connection()
                cursor = connection.cursor() 
                id_number = int(input("Enter index number: "))
                if cursor.execute('select * from products where product_id = %s', (id_number)):
                    items_list.append(id_number)
                else:
                    print("This index doesn not exists. Try again: ")
        except:
            print("Incorrect input. Try again: ")

def choose_courier():
    print_courier_db()
    while True:
        try:
            id_number = int(input("Enter id number: "))

            connection = get_db_connection()
            cursor = connection.cursor()     

            if cursor.execute('select * from couriers where courier_id = %s', (id_number)):
                return id_number
            else:
                print("Incorrect input: ID does not exist")
        except ValueError:
            print("Incorrect input. Enter index of the new courier: ")

def add_order_db():

    # 1. inputs
    #   - create choose_courier function for db
    #   - to check if customer exists if yes to request id if not to add to list and choose after. 
    # 2. add order_id & customer_id to orders
    # 3. add order_id & list of products with quantitites to orderproducts

    os.system("cls")

    customer_name = str(input("Enter name: "))
    customer_address = str(input("Enter customers address: "))
    customer_phone = str(input("Enter customers phone number: "))
    courier_id = choose_courier()
    items_list = add_product_index_to_list()

    #INSERT INTO table customer

    cust_dict = {
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone
    }

    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
        )
    cursor = connection.cursor()

    sql = '''INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES(%(customer_name)s,%(customer_address)s,%(customer_phone)s)'''
    cursor.execute(sql, cust_dict)

    connection.commit()

    customer_id = cursor.lastrowid
    print(customer_id)

    

    #INSERT INTO table customer

    order_dict = {
        "customer_id": customer_id,
        "courier_id": courier_id,
        "status": "PREPARING"
    }

    sql = "INSERT INTO orders(customer_id, courier_id, status) VALUES(%(customer_id)s, %(courier_id)s, %(status)s)"
    cursor.execute(sql, order_dict)

    connection.commit()

    order_id = cursor.lastrowid

    print(order_id)


    #INSERT INTO table order/products


    prods_dict = {}
    for item in items_list:
        prods_dict[item] = prods_dict.get(item, 0) +1

    
    
    # Transact order products
    sql = "INSERT INTO order_products(order_id, product_id, quantity) VALUES(%s, %s, %s)"
    sql_vals = [(order_id, key, value) for key, value in prods_dict.items()]
    cursor.executemany(sql, sql_vals)

    connection.commit()

    cursor.close()
    connection.close()


add_order_db()