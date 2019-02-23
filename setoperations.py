'''
Program to perform different set operations 
'''

def setoperations(s1, s2):
    set1, set2 = set(s1), set(s2)
    
    #union
    print("The union is :", set1|set2)
    
    #intersection
    print("The intersection is:", set1&set2)
    
    #difference
    print("The difference is:", set1-set2)
    
s1 = "They are"
s2 = "We are"
setoperations(s1, s2)
