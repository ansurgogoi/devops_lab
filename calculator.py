def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Add & Subtract Calculator")
print("-------------------------")
print("1. Add")
print("2. Subtract")

while True:
    choice = input("\nEnter choice (1/2) or 'q' to quit: ")

    if choice.lower() == 'q':
        break

    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    else:
        print("Invalid choice!")