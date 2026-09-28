def gcd(a, b):
    """Euclidean algorithm for greatest common divisor."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def prime_factors(n):
    if n < 2:
        raise ValueError("Enter an integer >= 2.")
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num


def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)

    bits = []
    while n:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


def character_to_number(ch):
    if len(ch) != 1:
        raise ValueError("Enter exactly one character.")
    return ord(ch)
