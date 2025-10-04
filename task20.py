def find_shortest_name_student(students: list) -> dict:
    return min(students, key=lambda x: len(x["name"]))
students1 = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
print(find_shortest_name_student(students1))
students2 = [
    {'name': 'Jo', 'age': 19},
    {'name': 'Ali', 'age': 20},
    {'name': 'Bob', 'age': 18}
]
print(find_shortest_name_student(students2))
