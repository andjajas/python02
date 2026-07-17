#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(
        self,
        default_msg: str = "Unknown plant error"
         ) -> None:
        super().__init__(default_msg)


class PlantError(GardenError):
    def __init__(
        self,
        default_msg: str = "The tomato plant is wilting!"
         ) -> None:
        super().__init__(default_msg)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(
            f"Invalid plant name to water: "
            f"'{plant_name}'"
        )


def test_watering_system(plant_names: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant_name in plant_names:
            water_plant(plant_name)
    except PlantError as e:
        print("Caught PlantError:", e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print("Cleanup always happens, even with errors!")
