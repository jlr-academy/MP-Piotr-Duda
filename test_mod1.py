import builtins
from main import product_menu, main_menu
from unittest.mock import Mock, patch
from unittest.mock import call
#from types import new_class
import os
import csv

@patch("main.product_menu")
@patch("builtins.input")
def test_print_list_with_index(mock_input: Mock, mock_list_with_index: Mock):
    #assembly
    mock_input.side_effect = ["1", "0"]
    
    #act
    list = [{'name': 'Coke Zero', 'price': '0.8'}]
    product_menu(list)

    #assert

    mock_list_with_index.assert_called_once() 


@patch("builtins.input")
def test_menu_option_0(mock_input: Mock):
#assemble

    new_dict = {"product_name":"Fanta", "product price": "1.2"}
    mock_input.side_effect = ["0"]
#act
    my_dict = {}
    main_menu(my_dict)
    if os.path.isfile("products.csv") and os.stat("products.csv").st_size != 0:
        with open("products.csv") as csv_file:
            reader = csv.reader(csv_file)
            my_dict = dict(reader)
#assert
    assert my_dict == new_dict