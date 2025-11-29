def generate_odd_series(n: int):
    if n <= 0:
        return []
    return [2*i - 1 for i in range(1, n+1)]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    series = generate_odd_series(n)
    print("Odd number series:", series)
