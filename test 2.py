print("==========================")
print("       Calculator")
print("==========================")

def calculate():
    if user_value == "+":
        print(num1 + num2)
    elif user_value == "-":
        print(num1 - num2)
    elif user_value == "*":
        print(num1 * num2)
    elif user_value == "/":
        print(num1 / num2)
    else:
        pass

try:
    user_value = input("Enter a opration (+, -, *, /): ")
    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the Second number: "))
except ValueError:
    print("wrong input")
except ZeroDivisionError:
    print("zero division error")
else:
    calculate()