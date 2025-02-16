#Python program to remove characters from a string
str = "Chocolate"
ch = "o"

print(str.replace(ch, '')) #Chclate

#Python Program to count occurrence of characters in string
str = "Mathematics"
ch = 't'
count = 0
for i in range(len(str)):
    if (str[i] == ch ):
        count += 1

print("Number of t in Mathematics is: ", count)

#
# Python program in to check string is anagrams or not
#anagrams - 1. a word or phrase made by transposing the letters of another word or phrase; The word "secure" is an anagram of "rescue."

#str1 = "secure"
#str2 = "rescue"
str1="Nope"
str2="oehN"
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Nope")