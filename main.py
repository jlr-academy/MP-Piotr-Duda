import os
from package1.module1 import *
from package1.module2 import *



def main_menu():

    while True:
        os.system("cls")
        print('''
        *****************************
        MAIN MENU
        *****************************
        0. Exit
        1. Product menu
        2. Courier menu
        3. Orders menu
        *****************************
        ''')

        try:
            choice = int(input("Select option 0-3: "))
            if choice == 0:
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
                print("Incorrect input. Select option 0-3: ")
        except ValueError:
            print("Incorrect input. Select option 0-3: ")
            
    
def product_menu():
    while True:
        print('''
        *****************************
        PRODUCT MENU
        *****************************
        0. Return to main menu
        1. Print products list
        2. Create new product
        3. Update existing product
        4. Delete product
        *****************************
        ''')


        try:
            choice = int(input("Select option 0/1/2/3/4: "))
            if choice == 0:
                break
            elif choice == 1:
                os.system("cls")
                print_products_db()
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
        print('''
        *****************************
        COURIER MENU
        *****************************
        0. Return to main menu
        1. Print courier list
        2. Create new courier
        3. Update existing courier
        4. Delete courier
        *****************************
        ''')

        try:
            choice = int(input("Select option 0 - 4: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                print_couriers_db()
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

def orders_menu():
    while True:
        os.system("cls")
        print('''
        *****************************
        ORDERS MENU
        *****************************
        0. Return to main menu
        1. Print orders
        2. Create new order
        3. Update order status
        4. Update order details
        5. Delete order
        *****************************
        ''')

        try:
            choice = int(input("Select option 0-5: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                print_orders_func()
            elif choice == 2:
                add_order_db()
            elif choice == 3:
                update_order_status_in_db()
            elif choice == 4:            
                update_order_db()
            elif choice == 5:
                delete_order_from_db()
            else:
                os.system("cls")
                print("Incorrect input. Select option 0-5: ")
        except ValueError:
            print("Incorrect input. Select option 0-5: ")

def customer_menu():
    while True:
        print('''
        *****************************
        COURIER MENU
        *****************************
        0. Return to main menu
        1. Print customer list
        2. Create new customer
        3. Update existing customer
        4. Delete customer
        *****************************
        ''')

        try:
            choice = int(input("Select option 0 - 4: "))
            if choice == 0:
                os.system("cls")
                break
            elif choice == 1:
                print_couriers_db()
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

if __name__ == "__main__":
    main_menu()     