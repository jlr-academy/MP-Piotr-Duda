import os
#from os import system
from package1.module1 import *
from package1.module2 import *
# create a function for opening the file and return a list and use that for both files

product_list = []
courier_list = []
orders_list = []


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
            choice = int(input("Select option 0-3: "))
            if choice == 0:
                save_files(product_list, courier_list, orders_list)
                break
            elif choice == 1:
                os.system("cls")
                product_menu(product_list)
            elif choice == 2:
                os.system("cls")
                courier_menu(courier_list)
            elif choice == 3:
                os.system("cls")
                orders_menu(product_list, courier_list, orders_list)
            else:
                print("Incorrect input. Select option 0-3: ")
        except ValueError:
            print("Incorrect input. Select option 0-3: ")
            
    
def product_menu(product_list):
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
                print(product_list)
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

def courier_menu(courier_list):
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
                print_list_with_index(courier_list)
            elif choice == 2:
                add_item(courier_list)
            elif choice == 3:
                update_list(courier_list)
            elif choice == 4:
                delete_item(courier_list)
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
                print_list_with_index(orders_list)
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

load_files(product_list, courier_list, orders_list)
main_menu()     