def count_words(text: str) -> dict:
    words = text.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

print(count_words("salom salom dunyo"))
print(count_words("Python python PYTHON"))
