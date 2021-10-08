from ..package1.module1 import *

def test_add_item(list):
    #assemble
    test_list = ["Bob", "Mark", "Andrew"]
    expected = ["Bob", "Mark", "Andrew", "John"]

    def mock_list():
        return test_list

    def mock_input():
        return "John"
    #act
    result = add_item(mock_list, mock_input)

    #assert

    assert result == expected
