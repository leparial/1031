#Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: \t")
second_input = input("Enter in second number: \t")
operation = input("Would you like to add/subtract/multiple/divide: \t")

first_number = float(first_input)
second_number = float(second_input)

""" An algorithm for calculating the Addition, Subtraction,
    Multiplication and Division
"""
def compute(first_number, second_number):  
  if operation == "add" or operation == "Add" or operation == "ADD":
    result = (first_number + second_number)
    return result

  elif operation == "subtract" or operation == "Subtract" or operation == "SUBTRACT":
    result = (first_number - second_number)
    return result 

  elif operation == "multiply" or operation == "Multiply" or operation == "MULTIPLY":
    result = (first_number * second_number)
    return result

  elif operation == "divide" or operation == "Divide" or operation == "DIVIDE":
    result = (first_number / second_number)
    return result
  else:
    return "Sorry, I do not understand your request."

print(compute(first_number, second_number))
