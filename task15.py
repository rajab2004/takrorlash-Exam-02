def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.values())
    students = [name for name, grade in grades.items() if grade == max_grade]
    return {"max_grade": max_grade, "students": students}

print(find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}))
print(find_top_students({"Aziz": 4, "Bobur": 5, "Diyor": 3}))
