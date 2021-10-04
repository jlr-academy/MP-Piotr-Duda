import os
from pack1.module1 import *
from pack1.module2 import *

# create a function for opening the file and return a list and use that for both files

product_list = []
courier_list = []


def main_menu():
    while True:
        print("*****************************")
        print("MAIN MENU")
        print("*****************************")
        print("0. Exit")
        print("1. Product menu")
        print("2. Courier menu")
        print("*****************************")

        try:
            choice = int(input("Select option 0/1/2:"))
            if choice == 0:
                save_files(product_list, courier_list)
                break
            elif choice == 1:
                os.system("cls")
                product_menu()
            elif choice == 2:
                os.system("cls")
                courier_menu()
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


def courier_menu():
    while True:
        print("*****************************")
        print("PRODUCT MENU")
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
                print(courier_list)
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


load_files(product_list, courier_list)
main_menu()