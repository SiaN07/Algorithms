def countChar(myString):
    
    count = {}
      
    for i in myString:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    print ("\n" + str(count))
            
countChar("aaabbddaabbcc")    