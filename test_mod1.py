import builtins
from unittest.mock import Mock, patch
from unittest.mock import call
import os
import csv
from package1.module1 import delete_item
from package1.module2 import convert_from_string_to_float_for_key_in_dictionary

def test_conversion_list_products_from_string_to_float():

    #assemble

    expected = [{'customer_name': 'Peter', 'customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'customer_phone': '0789887334', 'courier': 2, 'status': 'preparing', 'items': [2, 1, 1, 1, 0, 0]}, {'customer_name': 'Mark', 'customer_address': 'Birmingham', 'customer_phone': '987987987', 'courier': 2, 'status': 'preparing', 'items': [1]}]

    #act
    test_list = [{'customer_name': 'Peter', 'customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'customer_phone': '0789887334', 'courier': '2', 'status': 'preparing', 'items': '[2, 1, 1, 1, 0, 0]'}, {'customer_name': 'Mark', 'customer_address': 'Birmingham', 'customer_phone': '987987987', 'courier': '2', 'status': 'preparing', 'items': '[1]'}]
    result = convert_from_string_to_float_for_key_in_dictionary(test_list)

    #assert

    assert expected == result

@patch('builtins.input', side_effect = [0, 1])
def test_delete_item(mock_input: Mock):
    input_list = [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}]
    expected = [{2: 'b'}, {3: 'c'}, {4: 'd'}]

    result = delete_item(input_list)

    assert expected == result





#test_delete_item()
#test_conversion_list_products_from_string_to_float()