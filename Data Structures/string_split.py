msg = input('Enter a sentence : ')

words = msg.split()
print(words,len(words),"words found")

words = msg.split(',')
print(words,len(words),"words found")

word = msg.split('is')
print(words,len(words),"words found")

# what is the logic to get the last 3 words from a sentences?
print(msg.split()[-3:])