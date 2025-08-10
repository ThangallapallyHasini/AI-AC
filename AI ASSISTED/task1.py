def is_palindrome(sentence):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
sentence = input("Enter a sentence: ")
if is_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")