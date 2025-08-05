from math import pow as math_pow
from functools import lru_cache
from app.settings import settings


def _pow(x: float, y: float) -> float:
    return math_pow(x, y)

def _fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def _fact(n: int) -> int:
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

calculate_fibonacci = lru_cache(maxsize=128)(_fib) if settings.ENABLE_CACHE else _fib
calculate_factorial = lru_cache(maxsize=128)(_fact) if settings.ENABLE_CACHE else _fact
calculate_pow = lru_cache(maxsize=128)(_pow) if settings.ENABLE_CACHE else _pow