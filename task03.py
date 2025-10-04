def calculate_tax(salary: int) -> dict:
    if salary <= 5_000_000:
        rate, tax = "0%", 0
    elif salary <= 10_000_000:
        rate, tax = "12%", int(salary * 0.12)
    elif salary <= 20_000_000:
        rate, tax = "18%", int(salary * 0.18)
    else:
        rate, tax = "25%", int(salary * 0.25)
    return {"gross": salary, "tax": tax, "net": salary - tax, "rate": rate}

print(calculate_tax(8_000_000))
print(calculate_tax(3_000_000))
