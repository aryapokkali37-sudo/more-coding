a=int(input("first number"))
b=int(input("second number"))
def calc():
    q=input("|+|-|X|/|")
    if q=="+":
        def add(a,b):
            w=a+b
            print(w)
            return w
        print(add())
calc()