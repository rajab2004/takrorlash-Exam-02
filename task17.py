def filter_positive(numbers: list) -> list:
    return [d for d in numbers if d["value"] > 0]

print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))
print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))
