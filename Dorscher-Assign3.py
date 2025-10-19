def power(a: float, b: int) -> float:
    temp = 1.0
    for i in range(1, b + 1):
        temp *= a
    return temp

def power_functional(a: float, b: int) -> float:
    if (b==0):
        return 1.0
    return a * power_functional(a, b - 1) ## multiply 'a' each time for recursion

def power_tail(a: float, b: int, accumulator=1.0) -> float:
    if (b==0):
        return accumulator
    return power_tail(a, b - 1, a * accumulator) ## a is accumulated each time power_tail is called

def main():
    print("Power Function Iterative:")
    print(f"2^3 = {power(2, 3)}")
    print(f"5^0 = {power(5, 0)}")
    print(f"3^4 = {power(3, 4)}\n")

    print("Power Function Recursive:")
    print(f"2^3 = {power_functional(2, 3)}")
    print(f"5^0 = {power_functional(5, 0)}")
    print(f"3^4 = {power_functional(3, 4)}\n")

    print("Power Function Tail Recursive:")
    print(f"2^3 = {power_tail(2, 3)}")
    print(f"5^0 = {power_tail(5, 0)}")
    print(f"3^4 = {power_tail(3, 4)}\n")

    print("Power Function Built-in:")
    print(f"2^3 = {2.0 ** 3}")
    print(f"5^0 = {5.0 ** 0}")
    print(f"3^4 = {3.0 ** 4}\n")

    print("All methods give the same results.")


if __name__ == "__main__":
    main() 