from collections import defaultdict

def count_multiples(numbers: list, divisors=range(1, 10)):
    result = defaultdict(int)
    for divisor in divisors:
        result[divisor] = sum(1 for num in numbers if num % divisor == 0)
    return dict(result)

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    result = count_multiples(numbers)
    print("Multiples count:", result)
