# Recursive function that checks if a word is a palindrome or not
def is_paindrome(word):
    if len(word) <= 1:
        return True
    
    if first(word) == last(word):
        return is_paindrome(middle(word))
    
    else:
        return False
    
# Helper functions to obtain the first, last, and middle characters of a string
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# Usage
word = input("Enter a word to check if it's a palindrome:\n -> ")
if is_paindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
