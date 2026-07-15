#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(
            f"{temp_str}°C is too cold for plants (min 0°C)"
        )
    elif temp > 40:
        raise ValueError(
            f"{temp_str}°C is too hot for plants (max 40°C)"
        )
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    data: str = "25"
    print(f"Input data is '{data}'")
    try:
        temp: int = input_temperature(data)
        print(f"Temperature is now {temp} °C\n")
    except Exception as error:
        print("Caught input_temperature error:", error, "\n")
    data = "abc"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except Exception as error:
        print("Caught input_temperature error:", error, "\n")
    data = "100"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except Exception as error:
        print("Caught input_temperature error:", error, "\n")
    data = "-50"
    print(f"Input data is '{data}'")
    try:
        temp = input_temperature(data)
    except Exception as error:
        print("Caught input_temperature error:", error, "\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
