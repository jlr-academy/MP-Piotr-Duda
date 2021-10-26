import os
from package1.input_func import input_person_name
from .module2 import *
from .sql_queries import *
from .input_func import *

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









def add_product_to_db():

    # Load environment variables, establish a database connection and cursor
    
    connection = get_db_connection()

    cursor = connection.cursor()


    # Check if product existing in database. If not, add to database
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

    # Load environment variables, establish a database connection and cursor
    connection = get_db_connection()

    cursor = connection.cursor()


    # Check if product existing in database. If not, add to database
    name=input("Enter name: ")

    is_duplicate = check_courier_duplicates_in_db(name, cursor)

    if is_duplicate == True:
        print(name.title() + " already exists.")
    else:
        phone=int(input("Enter phone number: "))
        sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
        val = (name, phone)
        cursor.execute(sql, val)
        connection.commit()
    
    #Close cursor and connection
    cursor.close()
    connection.close()

def add_order_db(product_list, courier_list, orders_list):

    # 1. inputs
    #   - create choose_courier function for db
    #   - to check if customer exists if yes to request id if not to add to list and choose after. 
    # 2. add order_id & customer_id to orders
    # 3. add order_id & list of products with quantitites to orderproducts

    os.system("cls")
    print_list_with_index(orders_list)

    name = str(input_person_name())
    new_address = str(input("Enter customers address: "))
    new_phone = str(input("Enter customers phone number: "))
    new_courier = choose_courier()
    items_list = add_product_index_to_list(product_list)



    order_dict = {
        "customer_name": name.title(),
        "customer_address": new_address,
        "customer_phone": new_phone,
        "courier": new_courier,
        "status": "PREPARING"
    }

    sql = '''INSERT INTO orders (customer_name, custo'''

    cursor.execute(sql, order_dict)



    shopping_cart_dict = {}
    for item in items_list:
        shopping_cart_dict[item] = shopping_cart_dict.get(item, 0) +1

    
    
    # Transact order products
    sql = "INSERT INTO order_products(OrderID, ProductID, Quantity) VALUES(%s, %s, %s)"
    vals = [(order_id, key, value) for key, value in shopping_cart_dict.items()]
    cursor.execute(sql, vals)


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
            else:
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


