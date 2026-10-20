def fibonacci_series(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
