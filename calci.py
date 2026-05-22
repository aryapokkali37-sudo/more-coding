while True:
    print("the code calculator™")
    ope=input("chose an operator\n+\n-\n*\n/\n^\n√")
    if ope in listist:
        print("this is invalid please enter again")
    elif ope.isdigit():
         print("this is invalid please enter again")
    elif ope == "+":
        num1 = float(input("first number"))
        num2 = float(input("second number"))
        print(num1 + num2)
        break

    elif ope =="-":
        num1 = float(input("first number"))
        num2 = float(input("second number"))
        print(num1 - num2)
        break

    elif ope == "*":
        num1 = float(input("first number"))
        num2 = float(input("second number"))
        print(num1 * num2)
        break

    elif ope == "/":
        num1 = float(input("first number(to be divided)"))
        num2 = float(input("second number(to divide)"))
        print(num1 / num2)
        break 
    elif ope == "^":
        num1 = float(input("first number(base number)"))
        num2 = float(input("second number(power)"))
        print(num1 ** num2)
        break 
    elif ope == "√":
       num1 = float(input("number"))
       import math
       print((math.sqrt(num1)))
       break
    else:
       print("this is invalid please enter again")