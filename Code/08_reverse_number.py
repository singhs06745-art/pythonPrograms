def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])
