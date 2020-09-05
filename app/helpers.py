# Provides additional helper functions to your program
import json


def add(*argv):
    '''
    Adds all numbers together.
    Returns the result.

    If no arguments are provided, returns 0.
    '''
    sum = 0
    for num in argv:
        sum += num
    return sum


def to_json_decorator(func, *argv):
    '''
    Decorates a function to call the actual function and wrap its result
    in a simple json like this:

    {
        "value": "result"
    }

    Indent is set to 4 for easier readability.
    '''
    def json_func(*argv):
        result = func(*argv)

        # Create the result dictionary
        result_dict = {
            "value": result
        }

        # Convert the dictionary to a json string
        json_result = json.dumps(result_dict, indent=4)

        # return the string
        return json_result

    return json_func
