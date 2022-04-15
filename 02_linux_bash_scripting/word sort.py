vowels_words=[]
consonant=[]

while True:
    vowels=('a','e','i','o','u')
    word_add=input("give me a word, to quit, type quit: ").lower()

    if word_add =="quit":
        break
    
    if word_add.startswith(vowels):
        vowels_words.append(word_add)
    else:
        consonant.append(word_add)



vowels_words.sort()
print(vowels_words)

consonant.sort() 
print(consonant)