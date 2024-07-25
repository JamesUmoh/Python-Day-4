# Function to check if the remainder is even or odd
def check_remainder_even_odd(remainder):
    if remainder % 2 == 0:
        return "even"
    else:
        return "odd"

# Main program
def main():
    # Get the user's name
    user_name = input("Please enter your name: ")

    # Ask the user to enter two different numbers
    num1 = float(input(f"Hi {user_name}, please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # Divide the first number by the second number
    quotient = num1 / num2
    remainder = num1 % num2

    # Check if the remainder is even or odd
    remainder_status = check_remainder_even_odd(remainder)

    # Print the result
    print(f"{user_name}, the quotient of {num1} divided by {num2} is {quotient}.")
    print(f"The remainder is {remainder}, which is {remainder_status}.")

# Run the main program
if __name__ == "__main__":
    main()
