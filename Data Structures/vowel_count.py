# count the occurence of all vowels in a string

sentence = 'count the occurence of all vowels in a string'
for vowel in "aeiou":
    print(f"{vowel} counted {sentence.lower().count(vowel)} times")