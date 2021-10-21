import os
from .module2 import *
import pymysql
from dotenv import load_dotenv



#to add additiona parameter in the add_item function 
#to allow change field in a key in dictionary from price to phone
#to change new_price input for float when product to string when courier
def add_item(list):
    os.system("cls")
    new_name=input("Enter name: ")
    new_price=float(input("Enter price: "))
    new_dict={
        "name": new_name.title(),
        "price": new_price
    }
    is_duplicate = check_duplicates(list, new_name)
    if is_duplicate == True:
        print(new_name.title() + " already exists.")
    else:
        list.append(new_dict)
        print(new_dict)
        print(list)
        print("added to the list.")




def print_db(): 

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

    # Gets all rows from the result
    rows = cursor.fetchall()
    for row in rows:
        print(f'product_id: {row[0]}, product: {row[1]}, price: {row[2]}, quantity: {row[3]}')

    connection.commit()
    cursor.close()
    connection.close()




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
        in_stock=int(input("Enter number of items in stock: "))
        sql = "INSERT INTO products (name, price, in_stock) VALUES (%s, %s, %s)"
        val = (name, price, in_stock)
        cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()




def update_item_in_db():
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

    print_db()
    product_id = int(input("Enter ID"))

    cursor.execute('SELECT product_ID, name, price, in_stock FROM products')
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

    prod_price = float(input("Enter new price: "))
    if prod_price == "":
        pass
    else:
        sql = f"UPDATE products SET price = {prod_price} WHERE product_id = {product_id}"
        cursor.execute(sql)
        connection.commit()

    prod_stock = int(input("Enter new stock: "))
    if prod_stock == "":
        pass
    else:
        sql = f"UPDATE products SET in_stock = {prod_stock} WHERE product_id = {product_id}"
        cursor.execute(sql)
        connection.commit()

    cursor.close()
    connection.close()




def delete_item_from_db():
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
    print_db()
    id = int(input("Enter id: "))

    sql = f"DELETE FROM products WHERE product_id = {id}"
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()




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
            choice = int(input("choose 0/1: "))
            if choice == 0:
                print("The item has not been removed")
            elif choice == 1:
                print("The order has been deleted")
                list.remove(list[index])    
            else:
                print("This index does not exist. Try again")
        else:
            print("This index does not exists. Select existing index number:") 
    except ValueError:
        print("The input was not a number. Select existing index number: ") 




def add_order(product_list, courier_list, orders_list):
    os.system("cls")
    print_list_with_index(orders_list)

    new_name = str(input("Enter customers name: "))
    ### TO DO: add fuction for input of the address in required format
    new_address = str(input("Enter customers address: "))
    new_phone = str(input("Enter customers phone number: "))
    new_courier = str(choose_courier(courier_list))
    items_list = add_product_index_to_list(product_list)

    new_dictionary = {
        "customer_name": new_name.title(),
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




def update_order(product_list, courier_list, orders_list):
    os.system("cls")
    print_list_with_index(orders_list)
    index = int(input("Please enter index of the order to be ammended: "))
    
    os.system("cls")
    my_dict = orders_list[index]
    
    cust_name = str(input("Enter new customer name: "))
    if cust_name == "":
        pass
    else:
        my_dict["customer_name"] = cust_name

    cust_addr = str(input("Enter new customer address: "))
    if cust_addr == "":
        pass
    else:
        my_dict["customer_address"] = cust_addr

    cust_phon = str(input("Enter new customer phone number: "))
    if cust_phon == "":
        pass
    else:
        my_dict["customer_phone"] = cust_phon
 
    # add update asking if person wants to update courier and add below code to def
    
    my_dict["courier"] = str(choose_courier(courier_list))

    # to pack the below white True look into def as common with code in add order
    # also to add choice whether update asking if update is required
    my_dict["items"] = add_product_index_to_list(product_list)

    os.system("cls")
    print(f"The order has been updated - {my_dict}")