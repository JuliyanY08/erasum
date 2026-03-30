def apply_all(numbers, *functions):
    result_dict = {}
    for i in functions:
        if i == "sum":
            result_dict["sum"] = sum(numbers)
        elif i == "max":
            result_dict["max"] = max(numbers)
        elif i == "min":
            result_dict["min"] = min(numbers)
            
    return result_dict

print(apply_all([1, 3, 4], "sum", "max"))

