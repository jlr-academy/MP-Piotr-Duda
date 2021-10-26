import os
import pymysql
from dotenv import load_dotenv
from package1.sql_queries import *
from package1.module2 import *
import sys

print(sys.version)

def check_id_exists_db(id_number):
    connection = get_db_connection()
    cursor = connection.cursor()
    if cursor.execute('select * from products where product_id = %s', (id_number)):
        print("exists")
    else:
        print("doesn't exists")


# check_id_exists_db(5)

# @patch("main.product_menu")
# @patch("builtins.input")
# def test_print_list_with_index(mock_input: Mock, mock_list_with_index: Mock):
#     #assembly
#     mock_input.side_effect = ["1", "0"]
    
#     #act
#     list = [{'name': 'Coke Zero', 'price': '0.8'}]
#     product_menu(list)

#     #assert

#     mock_list_with_index.assert_called_once() 


# @patch("builtins.input")
# def test_menu_option_0(mock_input: Mock):
# #assemble

#     new_dict = {"product_name":"Fanta", "product price": "1.2"}
#     mock_input.side_effect = ["0"]
# #act
#     my_dict = {}
#     main_menu(my_dict)
#     if os.path.isfile("products.csv") and os.stat("products.csv").st_size != 0:
#         with open("products.csv") as csv_file:
#             reader = csv.reader(csv_file)
#             my_dict = dict(reader)
# #assert
#     assert my_dict == new_dict
