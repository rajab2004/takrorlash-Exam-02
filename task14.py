def find_pattern(items: list, pattern: str, match_type: str) -> list:
    pattern = pattern.lower()
    result = []
    for item in items:
        name = item.lower()
        if match_type == "starts" and name.startswith(pattern):
            result.append(item)
        elif match_type == "ends" and name.endswith(pattern):
            result.append(item)
        elif match_type == "contains" and pattern in name:
            result.append(item)
    return result

print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts"))
print(find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends"))
print(find_pattern(["Python", "Java", "JavaScript"], "java", "contains"))
