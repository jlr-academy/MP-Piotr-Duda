import builtins
from main import product_menu
from unittest.mock import Mock, patch
from unittest.mock import call

@patch("main.print_list_with_index")
@patch("builtins.input")
@patch("builtins.print")
def test_print_list_with_index(mock_print: Mock, mock_input: Mock, mock_list_with_index: Mock):
    #assembly
    mock_input.side_effect = ["1", "0"]
    
    #act
    list = ["Fanta", "Coca Cola, Sprite"]
    product_menu(list)

    #assert

    mock_list_with_index.assert_called_once() 