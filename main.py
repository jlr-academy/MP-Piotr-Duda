import os
from package1.module1 import *
from package1.module2 import *

# create a function for opening the file and return a list and use that for both files
orders_list = []
product_list = []
courier_list = []

def main_menu():

    load_files(product_list, courier_list, orders_list)

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
            choice = int(input("Select option 0-3: "))
            if choice == 0:
                save_files(product_list, courier_list, orders_list)
                break
            elif choice == 1:
                os.system("cls")
                product_menu()
            elif choice == 2:
                os.system("cls")
                courier_menu()
            elif choice == 3:
                os.system("cls")
                orders_menu(product_list, courier_list, orders_list)
            else:
                print("Incorrect input. Select option 0-3: ")
        except ValueError:
            print("Incorrect input. Select option 0-3: ")
            
    
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
            choice = int(input("Select option 0/1/2/3/4: "))
            if choice == 0:
                break
            elif choice == 1:
                os.system("cls")
                print_product_db()
            elif choice == 2:
                add_product_to_db()
            elif choice == 3:
                update_product_in_db()
            elif choice == 4:
                delete_product_from_db()
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
            choice = int(input("Select option 0 - 4: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                print_courier_db()
            elif choice == 2:
                add_courier_to_db()
            elif choice == 3:
                update_courier_in_db()
            elif choice == 4:
                delete_courier_from_db()
            else:
                os.system("cls")
                print("Incorrect input. Select option 0 - 4: ")
        except ValueError:
            os.system("cls")
            print("Incorrect input. Select option 0 - 4: ")

def orders_menu(product_list, courier_list, orders_list):
    while True:
        print("*****************************")
        print("ORDERS MENU")
        print("*****************************")
        print("0. Return to main menu")
        print("1. Print orders")
        print("2. Create new order")
        print("3. Update order status")
        print("4. Update order details")
        print("5. Delete order")
        print("*****************************")

        try:
            choice = int(input("Select option 0-5: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                # sorted_list = print_list_sorted(orders_list)
                # for item in sorted_list:
                #     print(item)
                print(orders_list)
            elif choice == 2:
                add_order(product_list, courier_list, orders_list)
            elif choice == 3:
                update_order_status(orders_list)
            elif choice == 4:            
                update_order(product_list, courier_list, orders_list)
            elif choice == 5:
                delete_item(orders_list)
            else:
                os.system("cls")
                print("Incorrect input. Select option 0-5: ")
        except ValueError:
            print("Incorrect input. Select option 0-5: ")

if __name__ == "__main__":
    main_menu()     