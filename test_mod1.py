import builtins
from main import product_menu, main_menu
from unittest.mock import Mock, patch
from unittest.mock import call
#from types import new_class
import os
import csv

from package1.module2 import convert_from_string_to_float_for_key_in_dictionary

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


def test_conversion_list_products_from_string_to_float():

    #assemble

    expected = [{'customer_name': 'Peter', 'customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'customer_phone': '0789887334', 'courier': 2, 'status': 'preparing', 'items': [2, 1, 1, 1, 0, 0]}, {'customer_name': 'Mark', 'customer_address': 'Birmingham', 'customer_phone': '987987987', 'courier': 2, 'status': 'preparing', 'items': [1]}]

    #act
    test_list = [{'customer_name': 'Peter', 'customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'customer_phone': '0789887334', 'courier': '2', 'status': 'preparing', 'items': '[2, 1, 1, 1, 0, 0]'}, {'customer_name': 'Mark', 'customer_address': 'Birmingham', 'customer_phone': '987987987', 'courier': '2', 'status': 'preparing', 'items': '[1]'}]
    result = convert_from_string_to_float_for_key_in_dictionary(test_list)

    #assert

    assert expected == result
