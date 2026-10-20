def missing_number(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    n = len(numbers) + 1
    return n * (n + 1) // 2 - sum(numbers)
