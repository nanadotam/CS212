def is_palindrome(word):
    # Base case: If the word is empty or contains only one character, it's a palindrome.
    if len(word) <= 1:
        return True
    
    # Check if the first and last characters of the word are the same.
    if first(word) == last(word):
        # Recursively check the middle part of the word.
        return is_palindrome(middle(word))
    
    # If the first and last characters are different, it's not a palindrome.
    return False

# Helper function to get the first character of a string.
def first(word):
    return word[0]

# Helper function to get the last character of a string.
def last(word):
    return word[-1]

# Helper function to get the middle part of a string (excluding the first and last characters).
def middle(word):
    return word[1:-1]

# Example usage:
word = "racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
