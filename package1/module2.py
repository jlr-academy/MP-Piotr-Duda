import json
from typing import List

def check_duplicates(list, new_item):
    for item in list:
        if new_item.upper() == item.upper():
            return True
    return False

def print_list_with_index(list: List):
    for item in range(len(list)):
        print(item, " - ", list[item])

def load_files(product_list: List, courier_list: List, json_list: List):
    product_file = open("data/products.txt", "r")
    for item in product_file.readlines():
        product_list.append(item.strip())
    product_file.close

    courier_file = open("data/couriers.txt", "r")
    for item in courier_file.readlines():
        courier_list.append(item.strip())
    product_file.close

    with open ("data/orders.json", "r") as file:
        json_object = json.load(file)
        json_list.extend(json_object)

def save_files(product_list, courier_list, json_list):
    with open("data/products.txt", "w") as prod_file_obj:
        for product in product_list:
            prod_file_obj.write(product + "\n")

    with open("data/couriers.txt", "w") as cour_file_obj:
        for courier in courier_list:
            cour_file_obj.write(courier + "\n")

    with open('data/orders.json', 'w') as f:
        json.dump(json_list, f)   