from collections import Counter

print(" Welcome to the Word Frequency Analysis App \n")

special_chars = [' ','1','2','3','4','5','6','7','8', '9', '0', '/','*','-','+','@','#','$','%', '.','?' ]
user_input = input("Please enter a word or a phrase  ").lower().strip()
for char in special_chars:
    user_input = user_input.replace(char, '')


user_input_len = len(user_input)
letters_count =  Counter(user_input)

print("\nYour Letters Frequency Table \n")
print("Letter  Occurrence Frequency")

for key, value in sorted(letters_count.items()):
    p = 100 * value / user_input_len
    p = round(p, 2)
    print(f" {key}  \t{value}  \t {p}%")


most_common_letters = letters_count.most_common()
lst = []
for i in most_common_letters:
    lst.append(i[0])

print("\nLetters ordered from highest to lowest in occurrence")
for letter in lst:
    print(letter, end=' ')

