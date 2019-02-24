'''
How many times a number occurs
'''
def countnum(array, num):
    count = 0
    n = len(array)
    for i in range(0, n):
        if (array[i] == num):
            count = count + 1
    return count
array = [1, 15, 20, 4, 15, 3,15]
num = 15
print(countnum(array, num))
    
