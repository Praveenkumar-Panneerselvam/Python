# Palindrome

def palindrome(main_string):
    reversed_string=""
    for i in main_string:
        reversed_string = i + reversed_string
    if(main_string == reversed_string):
        print(f"{main_string} is palindrome")
    else:
        print(f"{main_string} is not palindrome")
a=input("Enter a string : ")
palindrome(a)
