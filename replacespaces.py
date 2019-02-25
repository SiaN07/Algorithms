#replace spaces with %20

def spaces(string):
    if len(string) == 0:
        print("There is nothing")
    else:
        string1 = string.replace(" ", "%20")
        return string1
        
string = "hello world mama"
print(spaces(string))
