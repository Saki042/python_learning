#Reversing a String using an Extended Slicing Technique
example = 'I am learning Python - Day2'
reverted_example = example[::-1]
print(reverted_example)

#Counting Vowels in a Given Word
vowel = ['a', 'e', 'i', 'o', 'u']
print(type(vowel)) #list
word = 'borosil'
count = 0
print(type(word)) #string 
for i in word:
    if i in vowel:
        count += 1
print("No of vowels in borosil is: ", count)

# Convert a horizontal list into a vertical list with loop

horizontal_list = ['a', 'b', 'c'] 
vertical_string = '\n'.join(horizontal_list) 
print(vertical_string)