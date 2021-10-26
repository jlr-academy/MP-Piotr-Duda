import csv
import os
from typing import List
import ast
import pymysql
from dotenv import load_dotenv
from .sql_queries import *

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

# to be re-done requires join tables order/customer/orderproducts
# GET_ORDER_QUERY requires update and print statement
def print_order_db(): 

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(GET_ORDER_QUERY)

    # Gets all rows from the result
    rows = cursor.fetchall()
    for row in rows:
        print(f'order_id: {row[0]}, customer: {row[1]}, courier: {row[2]}, status: {row[3]}, items: {row[4]}')

    connection.commit()
    cursor.close()
    connection.close()

def print_order_by_id(id):
    os.system("cls")
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(GET_ORDER_QUERY)
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == id:
            print(f'order_id: {row[0]}, customer: {row[1]}, courier: {row[2]}, status: {row[3]}, items: {row[4]}')
    
    connection.commit()
    cursor.close()
    connection.close()

def check_duplicates(list, new_item):
    for item in list:
        if new_item.upper() == next(iter(item.values())).upper():
            return True
    return False

def check_product_duplicates_in_db(new_item, cursor):

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM products')

    # Gets all rows from the result
    rows = cursor.fetchall()

    for row in rows:
        if new_item.upper() == row[1].upper():
            connection.commit()
            cursor.close()
            connection.close()
            return True
    return False

    

def check_courier_duplicates_in_db(new_item, cursor):

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM couriers')

    # Gets all rows from the result
    rows = cursor.fetchall()

    for row in rows:
        if new_item.upper() == row[1].upper():
            connection.commit()
            cursor.close()
            connection.close()
            return True
    return False

def check_id_exists_db(id_number):
    connection = get_db_connection()
    cursor = connection.cursor()
    if cursor.execute('select * from products where product_id = %s', (id_number)):
        print("exists")
    else:
        print("doesn't exists")

def print_list_with_index(list: List):
    for item in range(len(list)):
        print(item, " - ", list[item])

def print_list_sorted(list: List):
    while True:
        try:
            index = int(input("Do you want sort list by courier - 0 or by status 1: "))
            if index == 0:
                sorted_list = sorted(list, key=lambda item: item['courier'])
                return sorted_list
            elif index == 1:
                sorted_list = sorted(list, key=lambda item: item['status'])
                return sorted_list
            else:
                print("Incorrect input. Enter 0 or 1")
        except ValueError:
            print("Incorrect input. Enter 0 or 1")  

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

def load_files(product_list: List, courier_list: List, orders_list: List):
    with open("data/products.csv", "r") as prod_obj:
        reader = csv.DictReader(prod_obj)
        product = list(reader)
        product_list.extend(product)
        

    with open("data/couriers.csv", "r") as cour_obj:
        reader = csv.DictReader(cour_obj)
        courier= list(reader)
        courier_list.extend(courier)

    with open("data/orders.csv", "r") as orde_obj:
        reader = csv.DictReader(orde_obj)
        orders = list(reader)
        orders_list.extend(orders)

    convert_from_string_to_float_for_key_in_dictionary(orders_list)


def save_files(product_list, courier_list, orders_list):
    
    with open("data/products.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(product_list)

    with open("data/couriers.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'phone'])
        writer.writeheader()
        writer.writerows(courier_list)

    with open("data/orders.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
        writer.writeheader()
        writer.writerows(orders_list)

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
        
def convert_from_string_to_float_for_key_in_dictionary(orders_list: List):
    new_order_list=[]
    for dict in orders_list:
        if dict["courier"] != "":
            dict["courier"] = int(dict["courier"])    
        if dict["items"] != "":
            dict["items"] = ast.literal_eval(dict["items"])
        new_order_list.append(dict)

    return new_order_list

def sql_to_csv():
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

    cursor = connection.cursor()

    cursor.execute('SELECT product_id, name, price, in_stock FROM products')

    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    fp = open('file.csv', 'w')
    myFile = csv.writer(fp)
    myFile.writerow(column_names)
    myFile.writerows(rows)
    fp.close()

    cursor.close()
    connection.close()

# sql_to_csv()    

# def csv_to_sql_db():
    # # Load environment variables from .env file
    # load_dotenv()
    # host = os.environ.get("mysql_host")
    # user = os.environ.get("mysql_user")
    # password = os.environ.get("mysql_pass")
    # database = os.environ.get("mysql_db")

    # # Establish a database connection
    # connection = pymysql.connect(
    #     host,
    #     user,
    #     password,
    #     database
    #     )

    # cursor = connection.cursor()
    # # csv_data = csv.reader(open("ile.csv"))
    # # next(csv_data)
    # # for row in csv_data:
    # #     cursor.execute("INSERT INTO import(name, price, in_stock) VALUES(%s, %s, %s) FIELDS TERMINATED BY ','", row)

    # Query = """ LOAD DATA LOCAL INFILE '\Users\pduda1\OneDrive\OneDrive - JAGUAR LAND ROVER\Documents\course\MP-Piotr-Duda\ile.csv' INTO TABLE
    # import FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED
    # BY '"' Lines terminated by '\n' IGNORE 1 LINES """

    # cursor.execute(Query)

    # connection.commit
    # cursor.close()
    # connection.close()

# # Transact order products
# sql_query = "INSERT INTO order_products(OrderID, ProductID, Quantity) VALUES(%s, %s, %s)"
# sql_vals =  vals = [(order_id, key, value) for key, value in shopping_cart_dict.items()]
# utils.db_transact(sql_query, sql_vals, False, True)