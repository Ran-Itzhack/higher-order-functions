
# HOR 2: Python Closures
# Nested Definitions
def make_adder(n: int) -> int:
    def adder(k: int) -> int:
        return k + n
    return adder