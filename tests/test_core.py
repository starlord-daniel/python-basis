import sys
import pytest
from context import app


class TestCore:
    def test_add_numbers(self):
        '''
        Test the app/core/ add_numbers() function.
        '''
        # arrange

        test_data = [
            {
                "expected": "{\n    \"value\": 0\n}",
                "args": []
            },
            {
                "expected": "{\n    \"value\": 1\n}",
                "args": [1]
            },
            {
                "expected": "{\n    \"value\": 4\n}",
                "args": [-1, 5]
            },
            {
                "expected": None,
                "args": [1, 2, 'a']
            }
        ]

        # act
        # assert
        for test in test_data:
            sys.argv[1:] = test["args"]
            actual = app.add_numbers()
            assert test["expected"] == actual

    def test_convert_console_args(self):
        '''
        Test the app/core/ convert_console_args() function.
        '''
        # arrange
        test_data = [
            {
                "expected": (),
                "args": []
            },
            {
                "expected": (1,),
                "args": ['1']
            },
            {
                "expected": (-1, 5),
                "args": ['-1', '5']
            },
            {
                "expected": (1, 5, 7),
                "args": ['1', '5', '7']
            }
        ]

        test_error_data = [
            {
                "expected": ValueError,
                "args": ['a']
            },
            {
                "expected": ValueError,
                "args": [1, 2, 'a']
            },
            {
                "expected": ValueError,
                "args": [-1, 'hallo', 200]
            }
        ]

        # act
        # assert
        for test in test_data:
            sys.argv[1:] = test["args"]
            args_map_object = app.convert_console_args()
            actual = tuple(args_map_object)
            assert test["expected"] == actual

        # check for raised errors
        with pytest.raises(ValueError) as err_info:
            for test in test_error_data:
                sys.argv[1:] = test["args"]
                args_map_object = app.convert_console_args()
                actual = tuple(args_map_object)
        assert err_info.type is test["expected"]
