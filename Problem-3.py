def conditional_odd_series(n: int):
    if n <= 0:
        return []

    count = n if n % 2 != 0 else n - 1
    return [2*i - 1 for i in range(1, count+1)]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    series = conditional_odd_series(n)
    print("Conditional odd series:", series)
