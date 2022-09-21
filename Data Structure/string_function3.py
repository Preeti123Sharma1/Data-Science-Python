# string validation

value = input("Enter the guest name:")

if value.startswith('Mr.'):
    print('Welcome sir')
elif value.startswith('Ms.'):
    print("Welcome Ma'am") 
elif value.startswith("Dr."):
    print("Welcome Doctor")
else:
    print("You are not invited")           