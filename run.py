# The entrypoint for your program
import app

if __name__ == "__main__":
    result = app.add_numbers()
    if result is not None:
        print(result)
