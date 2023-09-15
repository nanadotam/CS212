import math

def hypotenuse(a, b):
    c = round(math.sqrt(a**2 + b**2), 4)
    return c

def var_hyp():
    try:
        a = float(input("Enter a value for 'a': "))
        b = float(input("Enter a value for 'b': "))
       
        result = hypotenuse(a, b)
        print(result)
    except ValueError:
        print("Invalid input. Kindly enter valid figures for a and b😊")

var_hyp()