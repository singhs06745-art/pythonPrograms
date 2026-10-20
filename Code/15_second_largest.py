def second_largest(numbers):
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 2:
        raise ValueError("At least two distinct numbers required")
    return unique[1]
