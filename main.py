import numpy as np

def add(first_number, second_number):
    """
    Adds two numbers together.
    """
    result = np.add(first_number, second_number)
    return result

'''Create the starting point of the app'''
if __name__ == "__main__":
    #Ask user for the first number
    first_number = int(input("Enter the first number: "))
    #Ask user for the second number
    second_number = int(input("Enter the second number: "))
    #Now lets call our function and pass the two numbers
    result = add(first_number, second_number) 
    #Print the result
    print(f"The result of adding {first_number} + {second_number} is: {result}")
    