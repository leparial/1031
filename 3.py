# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: \t")
second_input = input("Enter in second number: \t")
operation = input("Would you like to add/subtract/multiple/divide: \t")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

# Calculating the given two terms
#Formula for Addtion
def calculator (first_number, second_number):
 if operation == "add" or operation == "Add" or operation == "ADD":
    result = (first_number + second_number)
    return result

# Formula for Subtraction
 elif operation == "subtract" or operation == "Subtract" or operation == "SUBTRACT":
    result = (first_number - second_number)
    return result 

#Formula for Multiplication
 elif operation == "multiply" or operation == "Multiply" or operation == "MULTIPLY":
    result = (first_number * second_number)
    return result

#Formula for Division
 elif operation == "divide" or operation == "Divide" or operation == "DIVIDE":
    result = (first_number / second_number)
    return result
 else:
    return "Sorry, I do not understand your request."
#Print Answer
print(calculator(first_number, second_number))
