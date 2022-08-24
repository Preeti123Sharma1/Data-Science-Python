# string validation function

value = input('enter someting:')

#test
if value.isnumeric():
    print("Only numbers", value.isnumeric())
if value.isalpha():
    print('On;y alphabets', value.isalpha())
if value.isalnum():
    print('Alphabets & numbers', value.isalnum())
if value.isspace():
    print('only space', value.isspace())
if value.isupper():
    print('uppercase alphabets', value.isupper())
if value.islower():
    print('lowercase alphabets', value.islower())       
