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
            print("Are you sure you want delete item: " + list[index])
            print("0. No")
            print("1. Yes")
            choice = int(input("choose 0/1: "))
            if choice == 0:
                print("The item has not been removed")
            elif choice == 1:
                print(list[index] + " has been removed.")
                list.remove(list[index])    
            else:
                print("This index does not exist. Try again")
        else:
            print("This index does not exists. Select existing index number:") 
    except ValueError:
        print("The input was not a number. Select existing index number: ") 
 
