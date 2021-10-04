def check_duplicates(list, new_item):
    for item in list:
        if new_item.upper() == item.upper():
            return True
    return False

def print_list_with_index(list):
    for item in range(len(list)):
        print(item, " - ", list[item])

def load_files(product_list, courier_list):
    product_file = open("products.txt", "r")
    for item in product_file.readlines():
        product_list.append(item.strip())
    product_file.close

    courier_file = open("couriers.txt", "r")
    for item in courier_file.readlines():
        courier_list.append(item.strip())
    product_file.close

def save_files(product_list, courier_list):
    with open("products.txt", "w") as prod_file_obj:
        for product in product_list:
            prod_file_obj.write(product + "\n")

    with open("couriers.txt", "w") as cour_file_obj:
        for courier in courier_list:
            cour_file_obj.write(courier + "\n")   