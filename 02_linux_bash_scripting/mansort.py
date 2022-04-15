word_list = []
vowel_list = []
consonant_list = []
vowel = "aeiou"

add_list = input("give me a word, to quit, type quit: ")

while add_list != "quit":
    word_list.append(add_list)

    
    add_list = input("give me a word, to quit, type quit: ")

else:
    print("you quit")
    print(word_list)




# if word_list.sort("aeiou") == True
#     vowel_list.append(word_list)
#     print(vowel_list)
