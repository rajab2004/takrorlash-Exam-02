def calculate_stats(numbers: list) -> dict:
    total = sum(numbers)
    avg = round(total / len(numbers), 2)
    return {"sum": total, "average": avg}

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
print(calculate_stats([10, 20, 30]))
