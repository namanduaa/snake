# Prime Number Checker Program

print("=" * 50)
print("        PRIME NUMBER CHECKER")
print("=" * 50)

while True:
    try:
        number = int(input("\nEnter a number (or -1 to exit): "))

        if number == -1:
            print("Thank you for using Prime Checker. Goodbye!")
            break

        if number < 2:
            print(f"✗ {number} is NOT a prime number")
            continue

        if number == 2:
            print(f"✓ {number} is a PRIME number")
            continue

        if number % 2 == 0:
            print(f"✗ {number} is NOT a prime number")
            continue

        is_prime = True
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"✓ {number} is a PRIME number")
        else:
            print(f"✗ {number} is NOT a prime number")

    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")