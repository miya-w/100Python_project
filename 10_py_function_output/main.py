# function with output

def my_function():
    result = 3 * 2
    return result


# .title() -> convert string to Title Case in python

# #Functions with Outputs
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   f"Result: {formated_f_name} {formated_l_name}"

# #Storing output in a variable
# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)
# #or printing output directly
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# #Already used functions with outputs.
# length = len(formatted_name)

# #Return as an early exit
# def format_name(f_name, l_name):
#   """Take a first and last name and format it 
#   to return the title case version of the name."""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

# Docstring using """ """ or  " # "
# example - - ->
"""
kjkhgtdfrdsehtrdjyyt
"""

# - - - - - - - - - - - 
# project - Calculator
# - - - - - - - - - - -

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
#   print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
