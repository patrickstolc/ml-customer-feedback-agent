from typing import Annotated, List

def calculate_average(values: Annotated[List[int], "A list of integers"]) -> Annotated[float, "The average of the list of integers"]:
    if not isinstance(values, list):
        raise ValueError("Input must be a list of integers. You've passed " + str(type(values)))
    
    if len(values) == 0:
        raise ValueError("No values provided")
    
    if any(value < 0 for value in values):
        raise ValueError("Negative values are not allowed")
    
    if any(value > 5 for value in values):
        raise ValueError("Values cannot be greater than 5")
    
    if any(value % 1 != 0 for value in values):
        raise ValueError("Values must be integers")

    return sum(values) / len(values)
