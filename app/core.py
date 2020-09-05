# should contain the main functionality of your program
import sys
from .helpers import add, to_json_decorator


def add_numbers():
    '''
    Reads all numbers given in the command line and adds them.

    Returns the output as simple json.

    E.g. run.py 1 2 3 should return:

    {
        "value": 6
    }
    '''
    try:
        args = convert_console_args()
        add_with_json = to_json_decorator(add)

        return add_with_json(*args)
    except ValueError:
        # The error is thrown here due to lazy eval of the map function
        print("Please only use numbers as input values!")


def convert_console_args():
    '''
    Reads the console arguments and converts them to int tuples

    Returns: A tuple of the input arguments as int
    '''
    arg_str_tuple = tuple(sys.argv[1:])
    arg_int_tuple = map(int, arg_str_tuple)
    return arg_int_tuple
