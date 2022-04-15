
# including additional wrinkle

numerals_dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
print(numerals_dict)
user_input=input("Please enter Roman Numerals: ").upper()
user_list=list(user_input)
user_list.reverse()
value_list=0
prior_value=0

for i in user_list:
    if i in numerals_dict:
        rom_value=numerals_dict[i]
        if rom_value < prior_value:
            value_list -= rom_value*2
        prior_value = rom_value
        print(rom_value)
        value_list += rom_value
        
print(f"The Roman Numeral value is {value_list}")