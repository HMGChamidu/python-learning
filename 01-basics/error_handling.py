try:
    first_num, last_num = input(
        "Enter two numbers separated by a space: "
    ).split()

    first_num = float(first_num)
    last_num = float(last_num)

    result = first_num / last_num
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero!")