#!/usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            1 / 0
        case 2:
            open("non_existing_file.txt")
        case 3:
            "42" + 42


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
