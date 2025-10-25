# reverse a string
def reverse(main_string):
    reverse_string=""
    for i in main_string:
        reverse_string=i+reverse_string
    print(reverse_string)
a=input("Enter a string : ")
reverse(a)
