# Write a function to check if a given string is a palindrome

def check_plaindrome(text):
    reversed_text = text.replace(" ","").lower()

    if reversed_text == reversed_text[::-1] :
       print(f" The given text {text} is palindrome ")
    else :
        print(f" The given text {text} is not a palindrome ")

text = str(input(" Enter a word :"))
check_plaindrome(text)