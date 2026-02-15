user_input= input("enter the number:")

try:
                number = int(user_input)
                print(f"the number is {number}")
except ValueError as ve:
                print("Error: input is not valid number. plrase enter an integer.")

