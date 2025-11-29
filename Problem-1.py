class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, choice: int):
        if choice == 1:
            return self.a + self.b
        elif choice == 2:
            return self.a - self.b
        elif choice == 3:
            return self.a * self.b
        elif choice == 4:
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid choice"

if __name__ == "__main__":
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        choice = int(input("Enter choice (1-4): "))

        calc = Calculator(a, b)
        print("Result:", calc.calculate(choice))

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
