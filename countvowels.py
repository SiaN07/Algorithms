'''
Count number of vowels in a string
'''

def countvowels(string):
    vowels = set('aeiouAEIOU')
    count  = 0
    
    for char in string:
        if char in vowels:
            count = count + 1
    print("The number of vowels is", count)
string = "The red pie"
countvowels(string)
