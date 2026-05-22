try:
    def meow():
        print("The Code Calculator™")

        import sys
        import math
        from pint import UnitRegistry

        sys.set_int_max_str_digits(0)

        u = UnitRegistry()

        while True:

            a = input(
                "\nMain Menu:\n"
                "c = calculator\n"
                "l = length unit converter\n"
                "no = exit\n"
            ).strip().lower()

            if a == "c":

                while True:

                    ope = input(
                        "\nchoose an operator +|-|*|/|^|√\n"
                        "a=armstrong calculator | d=digit counter | v=value counter\n"
                    ).strip().lower()

                    if ope.isdigit():
                        print("this is invalid please enter again")

                    elif ope == "+":
                        num1 = float(input("first number: "))
                        num2 = float(input("second number: "))
                        print(num1 + num2)

                    elif ope == "-":
                        num1 = float(input("first number: "))
                        num2 = float(input("second number: "))
                        print(num1 - num2)

                    elif ope == "*":
                        num1 = float(input("first number: "))
                        num2 = float(input("second number: "))
                        print(num1 * num2)

                    elif ope == "/":
                        num1 = float(input("first number (to be divided): "))
                        num2 = float(input("second number (to divide): "))

                        if num2 == 0:
                            print("cannot divide by zero")
                        else:
                            print(num1 / num2)

                    elif ope == "^":
                        num1 = float(input("base number: "))
                        num2 = float(input("power: "))
                        print(num1 ** num2)

                    elif ope == "√":
                        num1 = float(input("number: "))

                        if num1 < 0:
                            print("cannot take square root of negative number")
                        else:
                            print(math.sqrt(num1))

                    elif ope == "a":

                        num1 = int(input("number: "))
                        total = 0
                        temp = num1

                        while temp > 0:
                            digit = temp % 10
                            total += digit ** 3
                            temp //= 10

                        if num1 == total:
                            print(num1, "is an Armstrong number")
                        else:
                            print(num1, "is not an Armstrong number")

                    elif ope == "d":

                        while True:

                            meow = input("num: ")

                            if meow.isdigit():

                                meow = int(meow)
                                count = 0

                                while meow > 0:
                                    meow //= 10
                                    count += 1

                                print(count)
                                break

                            else:
                                print("invalid, enter again")

                    elif ope == "v":

                        amount = input("the amount of money: ")
                        amount = int(amount)

                        notes1 = amount % 1
                        notes10 = amount // 10
                        notes20 = amount // 20
                        notes30 = amount // 30
                        notes40 = amount // 40
                        notes50 = amount // 50
                        notes60 = amount // 60
                        notes70 = amount // 70
                        notes80 = amount // 80
                        notes90 = amount // 90
                        notes100 = amount // 100
                        notes200 = amount // 200
                        notes500 = amount // 500
                        notes1000 = amount // 1000

                        print(
                            "the number of notes of 10 is", notes10,
                            "\nthe number of notes of 20 is", notes20,
                            "\nthe number of notes of 30 is", notes30,
                            "\nthe number of notes of 40 is", notes40,
                            "\nthe number of notes of 50 is", notes50,
                            "\nthe number of notes of 60 is", notes60,
                            "\nthe number of notes of 70 is", notes70,
                            "\nthe number of notes of 80 is", notes80,
                            "\nthe number of notes of 90 is", notes90,
                            "\nthe number of notes of 100 is", notes100,
                            "\nthe number of notes of 200 is", notes200,
                            "\nthe number of notes of 500 is", notes500,
                            "\nthe number of notes of 1000 is", notes1000,
                            "\nthe remainder (if any) is", notes1
                        )

                    else:
                        print("invalid operator")
                        continue

                    opinion = input(
                        "\nuse the calculator again? (yes/no): "
                    ).strip().lower()

                    if opinion != "yes":
                        break

            elif a == "l":

                while True:

                    value = float(input("Enter value: "))

                    from_unit = input(
                        "From unit (meter, cm, km, inch, foot...): "
                    ).strip().lower()

                    to_unit = input("To unit: ").strip().lower()

                    try:
                        quantity = value * u(from_unit)
                        result = quantity.to(to_unit)
                        print("Result:", result)

                    except:
                        print("invalid units")

                    again = input(
                        "\nConvert another? (yes/no): "
                    ).strip().lower()

                    if again != "yes":
                        break

            elif a == "no":
                print("goodbye")
                break

            else:
                print(
                    """dude you were supposed to enter c, l, or no.
    ITS NOT THAT HARD TO UNDERSTAND BASIC 
    INSTRUCTIONS, PLEASE DUDE YOUR 2 BRAIN 
    CELLS ARE BOTH FIGHTING FOR 2nd PLACE,
    just use your common sense and read the 
    instructions again

    if you still dont understand then maybe 
    you should go back to school and learn 
    how to read and follow instructions"""
                )
    meow()
except:
    print("exception" \
    "")