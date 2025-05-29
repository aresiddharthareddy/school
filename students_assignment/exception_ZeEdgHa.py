input_number1=int(input("Enter a number: "))
input_number2=int(input("Enter another number: "))
def safe_divide(input_number1, input_number2):
    try:
        print(input_number1/input_number2)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except:
        print("An unexpected error occurred")
safe_divide(input_number1, input_number2)