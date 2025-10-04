def analyze_grades(students: dict) -> dict:
    grades = list(students.values())
    avg = sum(grades) / len(grades)
    above = [name for name, grade in students.items() if grade > avg]
    return {"average": round(avg, 2), "above_average": above}

print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))
