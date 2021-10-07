import os
from .module2 import *

def add_item(list):
    os.system("cls")
    new_item=input("Enter new name: ")
    is_duplicate = check_duplicates(list, new_item)
    if is_duplicate == True:
        # Print out
        print(new_item.title() + " already exists.")
    else:
        # Or add
        list.append(new_item.title())
        print(new_item.title() + " added to the list.")    

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



def add_order(json_list, courier_list):
    os.system("cls")
    print_list_with_index(json_list)

    cust_dict = str(input("Enter customers name: "))
    cust_addr_dict = str(input("Enter customers address: "))
    cust_pho_dict = str(input("Enter customers phone number: "))
    
    print_list_with_index(courier_list)
    index = int(input("Enter index number: "))
    if courier_list[index] in courier_list:
        cour_dict = courier_list[index]
    else:
        print("This index does not exist. Try again")

    new_dictionary ={"customer_name" : cust_dict, "customer_address" : cust_addr_dict, "customer_phone" : cust_pho_dict, "courier" : cour_dict, "status" : "preparing" }
    json_list.append(new_dictionary)
    
    
    

def update_order_status(json_list):
    
    print_list_with_index(json_list)
    index = int(input("Please enter index of the order to update status: "))
    my_dict = json_list[index]
    options = ["preparing", "awaiting shipment", "in transit", "delivered"]
    
    print("New status")
    print("0. preparing")
    print("1. awaiting shipment")
    print("2. in transit")
    print("3. delivered")
    
    index = int(input("Please enter index of the new status: "))
    my_dict["status"] = options[index]

def update_order(json_list, courier_list):
    print_list_with_index(json_list)
    index = int(input("Please enter index of the order to be ammended: "))
    my_dict = json_list[index]
    
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

    # how to approach 
    while True:
        try:
            print_list_with_index(courier_list)
            index = int(input("Enter index of the new courier"))
            
            if index in range(len(courier_list)):
                print(range(courier_list))
                my_dict["courier"] = courier_list[index]
                break
            else:
                print("Enter correct index number")    
        except ValueError:
            os.system("cls")
            print("The input was not a number. Select option 0-5: ")