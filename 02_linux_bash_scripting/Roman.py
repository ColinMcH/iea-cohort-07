numerals_dict={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, "I":1}
print(numerals_dict)

user_input=input("Please enter Roman Numberals: ")
user_list=list(user_input)

value_list=0
print(type(value_list))
for i in user_list:
    if i in numerals_dict:
        rom_value=numerals_dict[i]
        value_list += rom_value

print(f"The Roman Numeral value is {value_list}")


