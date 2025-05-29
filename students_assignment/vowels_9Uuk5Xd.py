input_string=list(input("Enter a string: "))
def vowels(input_string):

    vowels=['a','e','i','o','u']
    are_vowels=[]
    for i in input_string:
        if i in vowels:
            are_vowels.append(i)

    return are_vowels
print(input_string)
vowels1 = vowels(input_string)
print(vowels1)