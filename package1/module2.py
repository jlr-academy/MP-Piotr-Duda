import csv
import os
from typing import List

def check_duplicates(list, new_item):
    for item in list:
        if new_item.upper() == next(iter(item.values())).upper():
            return True
    return False

def print_list_with_index(list: List):
    for item in range(len(list)):
        print(item, " - ", list[item])

def choose_courier(courier_list):
    try:
        print_list_with_index(courier_list)
        index = int(input("Enter index number: "))
        if courier_list[index] in courier_list:
            new_courier = index
            return new_courier
        else:
            print("This index does not exist. Try again")
    except ValueError:
        os.system("cls")
        print("Incorrect input. Enter index of the new courier: ")

def add_product_index_to_list(product_list):
    items_list = []
    while True:
        try:
            choice = int(input("Do you want add products to the order? 0 - No / 1 - Yes"))
            if choice == 0:
                os.system("cls")
                return items_list
                #break
            elif choice == 1:
                print_list_with_index(product_list)
                index = int(input("Enter index number: "))
                if product_list[index] in product_list:
                    new_index = index
                    items_list.append(new_index)
                    print(items_list)
                else:
                    print("This index doesn not exists. Try again: ")
        except:
            print("Incorrect input. Try again: ")

def load_files(product_list: List, courier_list: List, orders_list: List):
    with open("data/products.csv", "r") as prod_obj:
        reader = csv.DictReader(prod_obj)
        product = list(reader)
        product_list.extend(product)
        

    with open("data/couriers.csv", "r") as cour_obj:
        reader = csv.DictReader(cour_obj)
        courier= list(reader)
        courier_list.extend(courier)

    with open("data/orders.csv", "r") as orde_obj:
        reader = csv.DictReader(orde_obj)
        orders = list(reader)
        orders_list.extend(orders)


def save_files(product_list, courier_list, orders_list):
    
    with open("data/products.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(product_list)

    with open("data/couriers.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'phone'])
        writer.writeheader()
        writer.writerows(courier_list)

    with open("data/orders.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items'])
        writer.writeheader()
        writer.writerows(orders_list) 