import os
from pack1.module1 import *
from pack1.module2 import *
# create a function for opening the file and return a list and use that for both files

product_list = []
courier_list = []
json_list = []


def main_menu():
    while True:
        print("*****************************")
        print("MAIN MENU")
        print("*****************************")
        print("0. Exit")
        print("1. Product menu")
        print("2. Courier menu")
        print("3. Orders menu")
        print("*****************************")

        try:
            choice = int(input("Select option 0-3:"))
            if choice == 0:
                save_files(product_list, courier_list, json_list)
                break
            elif choice == 1:
                os.system("cls")
                product_menu()
            elif choice == 2:
                os.system("cls")
                courier_menu()
            elif choice == 3:
                os.system("cls")
                orders_menu()
            else:
                print("Error. Try again")
        except ValueError:
            print("The input was not a valid integer.")
            
    
def product_menu():
    while True:
        print("*****************************")
        print("PRODUCT MENU")
        print("*****************************")
        print("0. Return to main menu")
        print("1. Print products list")
        print("2. Create new product")
        print("3. Update existing product")
        print("4. Delete product")
        print("*****************************")


        try:
            choice = int(input("Select option 0/1/2/3/4:"))
            if choice == 0:
                break
            elif choice == 1:
                # What happens with the clear command if you use this program on a mac?
                os.system("cls")
                print_list_with_index(product_list)
            elif choice == 2:
                add_item(product_list)
            elif choice == 3:
                update_list(product_list)
            elif choice == 4:
                delete_item(product_list)
            else:
                os.system("cls")
                print("Incorrect input. Select option 0/1/2/3/4: ")
        except ValueError:
            os.system("cls")
            print("The input was not a number. Select option 0/1/2/3/4: ")


def courier_menu():
    while True:
        print("*****************************")
        print("COURIER MENU")
        print("*****************************")
        print("0. Return to main menu")
        print("1. Print courier list")
        print("2. Create new courier")
        print("3. Update existing courier")
        print("4. Delete courier")
        print("*****************************")

        try:
            choice = int(input("Select option 0/1/2/3/4: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                os.system("cls")
                print_list_with_index(courier_list)
            elif choice == 2:
                add_item(courier_list)
            elif choice == 3:
                update_list(courier_list)
            elif choice == 4:
                delete_item(courier_list)
            else:
                os.system("cls")
                print("Incorrect input. Select option 0/1/2/3/4: ")
        except ValueError:
            os.system("cls")
            print("The input was not a number. Select option 0/1/2/3/4: ")

def orders_menu():
    while True:
        print("*****************************")
        print("ORDERS MENU")
        print("*****************************")
        print("0. Return to main menu")
        print("1. Print orders")
        print("2. Create new order")
        print("3. Update order status")
        print("4. Update order details")
        print("5. Delete courier")
        print("*****************************")

        try:
            choice = int(input("Select option 0-5: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                os.system("cls")
                print_list_with_index(json_list)
            elif choice == 2:
                add_order(json_list, courier_list)
            elif choice == 3:
                # UPDATE existing order status
                # PRINT orders list with its index values
                # GET user input for order index value
                # PRINT order status list with index values
                # GET user input for order status index value
                # UPDATE status for order

                update_order_status(json_list)
            elif choice == 4:
                # PRINT orders list with its index values
                # GET user input for order index value
                # FOR EACH key-value pair in selected order:
                # GET user input for updated property
                # IF user input is blank:
                # do not update this property
                # ELSE:
                # update the property value with user input
                
                update_order(json_list, courier_list)
            elif choice == 5:

                delete_item(json_list)
            else:
                os.system("cls")
                print("Incorrect input. Select option 0-5: ")
        except ValueError:
            os.system("cls")
            print("The input was not a number. Select option 0-5: ")

load_files(product_list, courier_list, json_list)
# print(json_list)
main_menu()     