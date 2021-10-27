import os

from .module2 import *
from .sql_queries import *



#PRODUCTS

def add_product_to_db():
 #function updated
    name=input("Enter name: ")
    is_duplicate = check_duplicates_in_db(GET_PRODUCT_NAME_QUERY, name)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        price=float(input("Enter price: "))
        in_stock=int(input("Enter number of items in stock: "))
        val = (name, price, in_stock)
        sql_execute(ADD_PRODUCT_QUERY, val)

def update_product_in_db():
    #TO DO: functions to be separated and moved to module2
    os.system("cls")
    
    print_products_db()

    product_id = int(input("Enter ID"))
    print_product_by_id(GET_PRODUCT_BY_ID_QUERY, product_id)

    prod_name = str(input("Enter new name: "))
    if prod_name == "":
        pass
    else:
        val = (prod_name, product_id)
        sql_execute(UPDATE_PRODUCT_NAME_QUERY, val)

    while True:
        try:
            prod_price = input("Enter new price: ")
            if float(prod_price):
                val = (prod_price, product_id)
                sql_execute(UPDATE_PRODUCT_PRICE_QUERY, val)
                break

        except ValueError:
            if not prod_price:
                break
            else:
                print(ValueError('Incorect input. Enter float for a new price or leave empty if the price stays the same: '))

    while True:
        try:
            prod_stock = input("Enter new quantity in stock: ")
            if int(prod_stock):
                val = (prod_stock, product_id)
                sql_execute(UPDATE_PRODUCT_STOCK_QUERY, val)
                break

        except ValueError:
            if not prod_stock:
                break
            else:
                print(ValueError('Incorect input. Enter integer for a new quantity in stock or leave empty if the quantity stays the same: '))
                pass

    print("Product has been updated")

def delete_product_from_db():
    #TO DO: input validation is required

    os.system("cls")

    print_products_db()

    id = int(input("Enter id: "))

    sql_execute(DELETE_PRODUCT_QUERY, id)

    print("Product has been deleted")



#COURIERS

def add_courier_to_db():
 #function updated
    name=input("Enter name: ")
    is_duplicate = check_duplicates_in_db(GET_COURIER_NAME_QUERY, name)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        phone=int(input("Enter phone number: "))
        val = (name, phone)
        sql_execute(ADD_COURIER_QUERY, val)

def update_courier_in_db():
 #TO DO: functions to be separated and moved to module2
    os.system("cls")
    
    print_couriers_db()

    courier_id = int(input("Enter ID"))
    print_courier_by_id(GET_COURIER_BY_ID_QUERY, courier_id)

    courier_name = str(input("Enter new name: "))
    if courier_name == "":
        pass
    else:
        val = (courier_name, courier_id)
        sql_execute(UPDATE_COURIER_NAME_QUERY, val)

    while True:
        try:
            courier_phone = input("Enter new phone: ")
            if float(courier_phone):
                val = (courier_phone, courier_id)
                sql_execute(UPDATE_COURIER_PHONE_QUERY, val)
                break

        except ValueError:
            if not courier_phone:
                break
            else:
                print(ValueError('Incorect input. Enter float for a new price or leave empty if the price stays the same: '))

    print("Courier has been updated")

def delete_courier_from_db():
    #TO DO: input validation is required

    os.system("cls")

    print_couriers_db()

    id = int(input("Enter id: "))

    sql_execute(DELETE_COURIER_QUERY, id)
    
    print("Courier has been deleted")



#ORDERS

def print_orders_func():
    #data validation for y could be moved to seperate functions and use in other functions across project
    os.system("cls")
    print_orders_db()
    choice = input("Press 'y' if you want to see more details?")
    if choice == "y":
        id_choice = int(input("Enter id number of the order you want to view"))
        os.system("cls")
        print_order_by_id(id_choice)
        print("------")
        print_list_products_by_id(id_choice)
        os.system("pause")
    else: 
        pass

def add_order_db():

    os.system("cls")

    #to create support function for 3 below entries
    customer_name = str(input("Enter name: "))
    customer_address = str(input("Enter customers address: "))
    customer_phone = str(input("Enter customers phone number: "))
    courier_id = choose_courier()
    status = "PREPARING"

    val = (customer_name, customer_address, customer_phone)
    customer_id = sql_execute_and_return_last_row_id(ADD_CUSTOMER_QUERY, val)

    print(customer_id)

    #INSERT INTO table customer

    
    val = (customer_id, courier_id, status)
    order_id = sql_execute_and_return_last_row_id(ADD_ORDER_QUERY, val)

    add_product_to_order(order_id)

    print("Order has been created.")

def update_order_status_in_db():

    os.system("cls")
    print_orders_db()
    order_id = int(input("Enter ID"))

    connection = get_db_connection()
    cursor = connection.cursor()

    print_order_by_id(order_id)

    options = ["preparing", "awaiting shipment", "in transit", "delivered"]
    
    print("Available options:")
    print("0. preparing")
    print("1. awaiting shipment")
    print("2. in transit")
    print("3. delivered")
    index = int(input("Please enter index of the new status: "))
    status = options[index]
    
    sql = f"UPDATE orders SET status = '{status}' WHERE order_id = {order_id}"
    cursor.execute(sql)
    connection.commit()

    cursor.close()
    connection.close()

    print("Product has been updated")

def update_order_db():

    os.system("cls")
    print_orders_db()
    order_id = int(input("Enter ID"))

    print_order_by_id(order_id)

    customer_id = get_customer_id_by_order_id(order_id)
    update_customer_name(customer_id)
    update_customer_address(customer_id)
    update_customer_phone(customer_id)  
    update_courier_in_order(order_id)
    update_products_in_order(order_id)

    print("Order has been updated")

def delete_order_from_db():

    os.system("cls")
    print_orders_db()

    connection = get_db_connection()
    cursor = connection.cursor()

    id = int(input("Enter id: "))

    sql = f"DELETE FROM order_products WHERE order_id = {id}"
    cursor.execute(sql)
    
    sql = f"DELETE FROM orders WHERE order_id = {id}"
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()
    
    print("Product has been deleted")



#CUSTOMERS



























def delete_item(list):
    os.system("cls")
    print("Index | Name")
    print_list_with_index(list)
    try:
        index = int(input("Enter index number: "))
        if list[index] in list:
            print("Are you sure you want delete item: ", list[index])
            print("0. No")
            print("1. Yes")
            try:
                choice = int(input("choose 0/1: "))
                if choice == 0:
                    print("The item has not been removed")
                elif choice == 1:
                    print("The order has been deleted")
                    list.remove(list[index])
                    return list    
            except:
                print("This index does not exist. Try again")
        else:
            print("This index does not exists. Select existing index number:") 
    except ValueError:
        print("The input was not a number. Select existing index number: ") 









