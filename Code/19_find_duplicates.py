def find_duplicates(items):
    seen, duplicates = set(), []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates
