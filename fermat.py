# Function checks if fermat's theorem holds
def check_fermat(a, b, c, n):
    if a**n + b**n == c**n and n > 2:
        return "Holy Smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."
    
# Reads values for a, b, c, and n from the user and passes it into check_fermat()
def value_fermat():
    try:
        a = int(input("Enter a value for 'a': "))
        b = int(input("Enter a value for 'b': "))
        c = int(input("Enter a value for 'c': "))
        n = int(input("Enter a value for 'n': "))

        result = check_fermat(a, b, c, n)
        print(result)
    except ValueError:
        print("Invalid input. Please enter valid integer values for a, b, c, and n.")

value_fermat()