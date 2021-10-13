import os
from .module2 import *

#to add additiona parameter in the add_item function 
#to allow change field in a key in dictionary from price to phone
def add_item(list):
    os.system("cls")
    new_name=input("Enter name: ")
    new_price=float(input("Enter price: "))
    new_dict={
        "name": new_name,
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

def update_list(list):
    os.system("cls")
    print("Index | Name")
    print_list_with_index(list)
    index = int(input("Enter index number: "))
    if list[index] in list:
        updated_item=str(input("Enter new name: "))
        for item in range(0, len(list)):
            if list[item] == list[index]:
                print(list[index] + " has been updated to " + updated_item.title())
                list[item] = updated_item.title()       
    else:
        print("This index does not exist. Try again")

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
    ### add fuction for input of the address in required format
    new_address = str(input("Enter customers address: "))
    new_phone = str(input("Enter customers phone number: "))
    new_courier = choose_courier(courier_list)
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
    
    my_dict["courier"] = choose_courier(courier_list)

    # to pack the below white True look into def as common with code in add order
    # also to add choice whether update asking if update is required
    my_dict["items"] = add_product_index_to_list(product_list)

    os.system("cls")
    print(f"The order has been updated - {my_dict}")