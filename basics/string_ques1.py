# wap to count all the characters in a string
# and display the output like
# a - 3
# n - 9
# '''
# z - 0

from string import ascii_lowercase

msg = 'Life before Death, Hope before Despair, Journey before Destination'
for char in ascii_lowercase:
    print(f'{char} - {msg.count(char)}')