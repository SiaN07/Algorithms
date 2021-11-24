def duplicateChar(string):
    duplicates = []
    for char in string:
        if string.count(char) > 1:
            duplicates.append(char)
            print(duplicates[0])
        else:
            pass

duplicateChar("string")
