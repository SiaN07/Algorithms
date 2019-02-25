#Check if all the characters of a string are the same 
def check(s):
    n = len(s)

    for i in range(n):
        if s[i] != s[i+1]:
            return False
        else:
            return True
s = "eeeee"
print(check(s))
