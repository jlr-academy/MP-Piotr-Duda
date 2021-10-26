import os

from package1.input_func import input_person_name
from .module2 import *
from .sql_queries import *
from .input_func import *

def add_product_to_db():

    connection = get_db_connection()
    cursor = connection.cursor()

    name=input("Enter name: ")
    is_duplicate = check_product_duplicates_in_db(name, cursor)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        price=float(input("Enter price: "))
        in_stock=int(input("Enter number of items in stock: "))
        sql = "INSERT INTO products (name, price, in_stock) VALUES (%s, %s, %s)"
        val = (name, price, in_stock)
        cursor.execute(sql, val)
        connection.commit()
    
    #Close cursor and connection
    cursor.close()
    connection.close()

def add_courier_to_db():

    connection = get_db_connection()
    cursor = connection.cursor()

    name=input("Enter name: ")

    is_duplicate = check_courier_duplicates_in_db(name, cursor)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        #to create support function to run below sql
        phone=int(input("Enter phone number: "))
        sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        cursor.execute(sql, val)
        connection.commit()
    
    #Close cursor and connection
    cursor.close()
    connection.close()

def add_order_db():

    os.system("cls")

    #to create support function for 3 below entries
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

    connection = get_db_connection()
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

    ### HOW TO GET QUANTITIES ADDED REMOVED FROM INVENTORY

    # sql = "UPDATE products SET quantity = %s WHERE product_id = %s"
    # sql_vals = [(key, value) for key, value in prods_dict.items()]

    # connection.commit()

    cursor.close()
    connection.close()

def update_product_in_db():
    
    os.system("cls")
    print_product_db()
    product_id = int(input("Enter ID"))

    connection = get_db_connection()
    cursor = connection.cursor()

    os.system("cls")
    cursor.execute(GET_PRODUCTS_QUERY)
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == product_id:
            print(f'product_id: {row[0]}, product: {row[1]}, price: {row[2]}, quantity: {row[3]}')

    prod_name = str(input("Enter new name: "))
    if prod_name == "":
        pass
    else:
        sql = f"UPDATE products SET name = '{prod_name}' WHERE product_id = {product_id}"
        cursor.execute(sql)
        connection.commit()

    while True:
        try:
            prod_price = input("Enter new price: ")
            if float(prod_price):
                sql = f"UPDATE products SET price = {prod_price} WHERE product_id = {product_id}"
                cursor.execute(sql)
                connection.commit()
                break

        except ValueError:
            if not prod_price:
                break
            else:
                print(ValueError('Incorect input. Enter float for a new price or leave empty if the price stays the same: '))

    while True:
        try:
            prod_quant = input("Enter new quantity in stock: ")
            if int(prod_quant):
                sql = f"UPDATE products SET in_stock = {prod_quant} WHERE product_id = {product_id}"
                cursor.execute(sql)
                connection.commit()
                break

        except ValueError:
            if not prod_quant:
                break
            else:
                print(ValueError('Incorect input. Enter integer for a new quantity in stock or leave empty if the quantity stays the same: '))
                pass
    
    cursor.close()
    connection.close()

    print("Product has been updated")

def update_courier_in_db():

    os.system("cls")
    print_courier_db()
    courier_id = int(input("Enter ID"))

    connection = get_db_connection()
    cursor = connection.cursor()

    os.system("cls")
    cursor.execute(GET_COURIER_QUERY)
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == courier_id:
            print(f'courier_id: {row[0]}, courier: {row[1]}, phone: {row[2]}')

    cour_name = str(input("Enter new name: "))
    if cour_name == "":
        pass
    else:
        sql = f"UPDATE couriers SET name = '{cour_name}' WHERE courier_id = {courier_id}"
        cursor.execute(sql)
        connection.commit()

    while True:
        try:
            cour_phone = input("Enter new phone number: ")
            if int(cour_phone):
                sql = f"UPDATE couriers SET phone = {cour_phone} WHERE courier_id = {courier_id}"
                cursor.execute(sql)
                connection.commit()
                break

        except ValueError:
            if not cour_phone:
                break
            else:
                print(ValueError('Incorect input. Enter integer for a new phone number or leave empty if the phone number stays the same: '))


    cursor.close()
    connection.close()

    print("Product has been updated")

def update_order_status_in_db():

    os.system("cls")
    print_order_db()
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
    print_order_db()
    order_id = int(input("Enter ID"))

    connection = get_db_connection()
    cursor = connection.cursor()

    print_order_by_id(order_id)

    sql = GET_CUSTOMERID_FOR_ORDER_QUERY
    val = order_id
    cursor.execute(sql, val)
    row = cursor.fetchone()
    customer_id = row[0]
    
    #UPDATE CUSTOMER NAME
    customer_name = str(input("Enter new customer name: "))
    if customer_name == "":
        pass
    else:
        sql = f"UPDATE customers SET customer_name = '{customer_name}' WHERE customer_id = {customer_id}"
        cursor.execute(sql)
        connection.commit()
    
    #UPDATE CUSTOMER ADDRESS
    customer_address = str(input("Enter new customer address: "))
    if customer_name == "":
        pass
    else:
        sql = f"UPDATE customers SET customer_address = '{customer_address}' WHERE customer_id = {customer_id}"
        cursor.execute(sql)
        connection.commit()

    #UPDATE CUSTOMER PHONE NUMBER
    while True:
        customer_phone = input("Enter new phone number: ")
        if int(customer_phone):
            sql = f"UPDATE customers SET customer_phone = {customer_phone} WHERE customer_id = {customer_id}"
            cursor.execute(sql)
            connection.commit()
            break
        elif customer_phone == "":
            break
        else:
            print("Incorrect input: number required")
        
    
    #UPDATE COURIER

    courier_id = choose_courier()
    sql = f"UPDATE orders SET courier_id = '{courier_id}' WHERE order_id = {order_id}"
    cursor.execute(sql)
    connection.commit()

    #UPDATE PRODUCTS

    items_list = add_product_index_to_list()

    prods_dict = {}
    for item in items_list:
        prods_dict[item] = prods_dict.get(item, 0) +1

    # Transact order products
    sql = "DELETE FROM order_products WHERE order_id = %s"
    val = order_id
    cursor.execute(sql, val)
    connection.commit()

    sql = "INSERT INTO order_products(order_id, product_id, quantity) VALUES(%s, %s, %s)"
    sql_vals = [(order_id, key, value) for key, value in prods_dict.items()]
    cursor.executemany(sql, sql_vals)
    connection.commit()
    
    cursor.close()
    connection.close()

    print("Order has been updated")


def delete_product_from_db():

    os.system("cls")

    print_product_db()
    id = int(input("Enter id: "))

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = f"DELETE FROM products WHERE product_id = {id}"
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()

    print("Product has been deleted")

def delete_courier_from_db():

    os.system("cls")
    print_courier_db()

    connection = get_db_connection()

    cursor = connection.cursor()

    id = int(input("Enter id: "))

    sql = f"DELETE FROM couriers WHERE courier_id = {id}"
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()
    
    print("Product has been deleted")

def delete_order_from_db():

    os.system("cls")
    print_order_db()

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




#to upgrade naming for input and key in dictionary for product and courier
def update_list(list):
    os.system("cls")
    print("Index | Name")
    print_list_with_index(list)
    index = int(input("Enter index number: "))

    os.system("cls")
    my_dict = list[index]
    
    cust_name = str(input("Enter new name: "))
    if cust_name == "":
        pass
    else:
        my_dict["name"] = cust_name

    cust_name = str(input("Enter phone number: "))
    if cust_name == "":
        pass
    else:
        my_dict["phone"] = cust_name




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




def add_order(product_list, courier_list, orders_list):
    os.system("cls")
    print_list_with_index(orders_list)

    name = str(input_person_name())
    new_address = str(input("Enter customers address: "))
    new_phone = str(input("Enter customers phone number: "))
    new_courier = str(choose_courier(courier_list))
    items_list = add_product_index_to_list(product_list)

    new_dictionary = {
        "customer_name": name.title(),
        "customer_address": new_address,
        "customer_phone": new_phone,
        "courier": new_courier,
        "status": "PREPARING",
        "items": list(items_list)
    }
    orders_list.append(new_dictionary)


def update_order_status(orders_list):
    os.system("cls")
    print_list_with_index(orders_list)
    index = int(input("Please enter index of the order to update status: "))
    my_dict = orders_list[index]
    options = ["preparing", "awaiting shipment", "in transit", "delivered"]
    os.system("cls")
    print("Available options:")
    print("0. preparing")
    print("1. awaiting shipment")
    print("2. in transit")
    print("3. delivered")
    
    index = int(input("Please enter index of the new status: "))
    my_dict["status"] = options[index]
    status = my_dict["status"]
    os.system("cls")
    print(f"The status of the order has been updated to {status}")

def print_order_func():
    os.system("cls")
    print_order_db()
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





