# Application documentation

Code documentation should always happen within the code itself. This document is only intended to explain what is done.

## Functionality

The application is able to take any number of numbers from the command line as inputs and add them together. The result is returned in form of a simple json.

A sample call (from the project root) can look like this:

```bash
python run.py 1 2 3
```

Which will result in the following json:

```json
{
    "value": 6
}
```

## Tests

Testing is done with Pytest. To execute tests, use one of the following commands from the project root:

```bash
# using the Makefile
make test

# using pytest directly
pytest tests --cov=app tests/
```

## Linting

For this project, flake8 was chosen as a linter. To configure the linter, use the [setup.cfg](../setup.cfg) file. More information on flake8 configuration can be found in the [flake8 documentation](https://flake8.pycqa.org/en/latest/user/configuration.html)

The linter typically evaluates code as you write, but to call it explicitly, use one of the following commands from the project root:

```bash
# using the Makefile
make lint

# using pytest directly
flake8
```
