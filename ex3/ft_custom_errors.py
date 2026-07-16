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


class WaterError(GardenError):
    def __init__(
        self,
        default_msg: str = "Not enough water in the tank!"
         ) -> None:
        super().__init__(default_msg)


def raise_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        print("Testing PlantError...")
        raise PlantError()
    except PlantError as error:
        print("Caught PlantError:", error)


if __name__ == "__main__":
    raise_errors()