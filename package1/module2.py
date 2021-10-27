import csv
import os
from typing import List
import ast
import pymysql
from dotenv import load_dotenv
from .sql_queries import *
from .db_func import *

def print_products_db():
    #done

    rows = sql_read(GET_PRODUCTS_QUERY)

    for row in rows:
        print(f'product_id: {row[0]}, product: {row[1]}, price: {row[2]}, stock: {row[3]}')


def print_product_by_id(sql, val): 
    #done
    rows = sql_read(sql, val)

    for row in rows:
        print(f'product_id: {row[0]}, product: {row[1]}, price: {row[2]}, stock: {row[3]}')

def print_couriers_db(): 
    #done
    rows = sql_read(GET_COURIER_QUERY)

    for row in rows:
        print(f'courier_id: {row[0]}, courier: {row[1]}, phone: {row[2]}')

def print_courier_by_id(sql, val): 
    #done
    rows = sql_read(sql, val)

    for row in rows:
        print(f'courier_id: {row[0]}, courier: {row[1]}, phone: {row[2]}')

def print_orders_db(): 
    #done
    rows = sql_read(GET_ORDER_QUERY)
    for row in rows:
        print(f'order_id: {row[0]} |customer: {row[1]}, {row[2]}, {row[3]} | courier: {row[4]} | status: {row[5]} | items: {row[6]}')

def print_order_by_id(id):
    #done
    rows = sql_read(GET_ORDER_QUERY)

    for row in rows:
        if row[0] == id:
            print(f'order_id: {row[0]} |customer: {row[1]}, {row[2]}, {row[3]} | courier: {row[4]} | status: {row[5]} | items: {row[6]}')
    
def print_customers_db():

    rows = sql_read(GET_COURIER_QUERY)

    for row in rows:
        print(f'courier_id: {row[0]}, courier: {row[1]}, phone: {row[2]}')


def print_list_products_by_id(id):
    #done
    rows = sql_read(GET_ORDER_PRODUCTS_QUERY, id)

    for row in rows:
        print(f'product id: {row[0]} | product name: {row[1]} | quantity: {row[2]}')



def check_duplicates_in_db(sql, item_name):
#function updated
    rows = sql_read(sql)

    for row in rows:
        if item_name.upper() == row[0].upper():
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
    print_couriers_db()
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

    

def add_product_to_order(order_id):
    while True:
        print_products_db()
        product_id = product_id_check("\n Enter product ID: ")
        quantity = product_stock_check(product_id, "Enter quantity: ")
        data = (order_id, product_id, quantity)
        sql = """INSERT INTO order_products(order_id, product_id, quantity) 
                VALUES(%s, %s, %s)"""
        sql_execute(sql, data)

        add_more = task_choice("\n Please enter 'y' if you want to add more products: ")
        if add_more == False:
            break
        else:
            pass

def product_id_check(details: str):
    
    while True:
        id_choice = input(details)
        sql = "SELECT product_id FROM products WHERE product_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \tProduct with Id: {id_choice} doesn't exists. Please try again...")
            continue
        else:
            return id_choice

def product_stock_check(product_id, details: str):
    
    while True:
        print_product_by_id(GET_PRODUCT_BY_ID_QUERY, product_id)
        qty_choice = int(input(details))
        sql = "SELECT in_stock FROM products WHERE product_id=%s"
        rows = sql_read(sql, product_id)
        for row in rows:
            qty_check = row[0] 
        if qty_choice > qty_check:
            print(f"\n \tThere isn't enough in stock. Please use smaller amount...")
            os.system("pause")
            continue
        else:
            sql = """UPDATE products set in_stock = %s where product_id = %s"""
            reduced_stock = qty_check - qty_choice
            data = (reduced_stock, product_id)
            sql_execute(sql, data)
            return qty_choice


    # items_list = []
    # while True:
    #     try:
    #         choice = int(input("Do you want add products to the order? 0 - No / 1 - Yes"))
    #         if choice == 0:
    #             os.system("cls")
    #             return items_list
    #             #break
    #         elif choice == 1:
    #             print_product_db()
    #             connection = get_db_connection()
    #             cursor = connection.cursor() 
    #             id_number = int(input("Enter index number: "))
    #             if cursor.execute('select * from products where product_id = %s', (id_number)):
    #                 items_list.append(id_number)
    #             else:
    #                 print("This index doesn not exists. Try again: ")
    #     except:
    #         print("Incorrect input. Try again: ")



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



def task_choice(input_text):
    while True:
        user_choice = input(input_text).lower()
        if user_choice == 'y':
            return True
        else:
            return False

def update_customer_name(customer_id):

    customer_name = str(input("Enter new customer name: "))
    if customer_name == "":
        pass
    else:
        val = (customer_name, customer_id)
        sql_execute(UPDATE_CUSTOMER_NAME_QUERY, val)

def update_customer_address(customer_id):
    customer_address = str(input("Enter new customer address: "))
    if customer_address == "":
        pass
    else:
        val = (customer_address, customer_id)
        sql_execute(UPDATE_CUSTOMER_ADDRESS_QUERY, val)

def update_customer_phone(customer_id):
    while True:
        customer_phone = input("Enter new phone number: ")
        if not customer_phone:
            break
        elif int(customer_phone):
            val = (customer_phone, customer_id)
            sql_execute(UPDATE_CUSTOMER_PHONE_QUERY, val)
            break          
        else:
            print("Incorrect input: number required")

def update_courier_in_order(order_id):
    courier_id = choose_courier()
    val = (courier_id, order_id)
    sql_execute(UPDATE_ORDER_COURIER, val)

def update_products_in_order(order_id):
    sql_execute(DELETE_PRODUCTSORDERS_QUERY, order_id)
    add_product_to_order(order_id)

def get_customer_id_by_order_id(order_id):
    rows = sql_read(GET_CUSTOMERID_FOR_ORDER_QUERY, order_id)
    for row in rows:
        customer_id = row[0]
        return customer_id
