#!/usr/bin/env python3
def input_temperature(temp_str) -> int:
	temp = int(temp_str)
	return(temp)


def test_temperature() -> None:
	input_temperature("25")
	input_temperature("abc")