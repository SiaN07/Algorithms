def maxcount(array):
    n = len(array)
    count = 0 
    result = 0 
    
    for i in range(0, n):
        if (array[i] == 1):
            count = 0 
        else: 
            count += 1 
            result = max(result, count)
    
    return result
        
array = [0,1,0,0,1,1,1,0,0,0,0,0,1,1]
print(maxcount(array))
