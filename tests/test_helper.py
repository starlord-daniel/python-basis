from context import app


class TestHelpers:
    def test_add(self):
        '''
        Test the app/helpers/ add(*argv) function.

        The function can take a different number of args,
        so we should test multiple variants of calling it.
        '''
        # arrange
        test_data = [
            {"expected": 0, "args": ()},
            {"expected": 3, "args": (1, 2)},
            {"expected": 4, "args": (-1, 5)},
            {"expected": 6, "args": (1, 2, 3)},
            {"expected": 6, "args": (0, 1, 2, 3)},
            {"expected": 89, "args": (9, 5, 20, 26, 9, 20)}
        ]

        # act
        # assert
        for test in test_data:
            actual = app.add(*test["args"])
            assert test["expected"] == actual

    def test_to_json_decorator(self):
        '''
        Test the app/helpers/ to_json_decorator(func, *argv) function.
        '''
        # arrange
        test_pos_data = [
            {
                "expected": "{\n    \"value\": 3\n}",
                "func": app.add,
                "args": (1, 2)
            },
            {
                "expected": "{\n    \"value\": 0\n}",
                "func": app.add,
                "args": ()
            },
            {
                "expected": "{\n    \"value\": 6\n}",
                "func": app.add,
                "args": (1, 2, 3)
            }
        ]

        # act
        # assert
        for test in test_pos_data:
            decorated_func = app.to_json_decorator(test["func"])
            actual = decorated_func(*test["args"])
            assert test["expected"] == actual
