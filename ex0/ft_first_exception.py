#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    data: str = "25"
    print(f"Input data is '{data}'")
    try:
        temp: int = input_temperature(data)
        print(f"Temperature is now {temp} °C")
    except Exception as error:
        print("Caught input_temperature error:", error)
    print()
    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except Exception as error:
        print("Caught input_temperature error:", error)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
