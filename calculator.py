# Define arithmetic functions that take two parameters
# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division 
def divide(x, y):
    # Prevent division by zero
    if y == 0:
        print("Oops! Can't divide by zero. Try another number.")
        return None
    return x / y

# Input statements for user
print("Hi there! Welcome to our friendly calculator.")

print("What operation would you like to do?")
print("Type + for addition, - for subtraction, * for multiplication, or / for division.")
operation = input()

first_number = float(input("Enter  the first term: "))
second_number = float(input("Enter the second term: "))


# Let's do the math based on what the user chose.
if operation == '+':
    print(f"The result of adding {first_number} and {second_number} is: ", add(first_number, second_number))
elif operation == '-':
    print(f"The result of subtracting {first_number} and {second_number} is: ", subtract(first_number, second_number))
elif operation == '*':
    print(f"The result of multiplying {first_number} and {second_number} is: ", multiply(first_number, second_number))
elif operation == '/':
    result = divide(first_number, second_number)
    if result is not None:  # Making sure we don't print anything if division by zero was attempted.
        print(f"The result of dividing {first_number} and {second_number} is: ", result)
else:
    print("Hmm, I didn't get that. Make sure to choose a correct mathematical function.")

# And that's it! Simple calculator!
