from collections import Counter
def analyze_list(items: list) -> dict:
    total = len(items)
    unique = len(set(items))
    counts = Counter(items)
    duplicates = [item for item, count in counts.items() if count > 1]
    most_common = counts.most_common(1)[0][0]
    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common
    }

print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))
