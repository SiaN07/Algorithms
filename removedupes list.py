# Python 3 program to remove the
# duplicates from the array
def removeDups(arr):
    nums = []
    for i in arr:
        if i not in nums:
            nums.append(i)
    return nums
            

# Driver code
arr = [ 1, 2, 5, 1, 7, 2, 4, 2 ]


print(removeDups(arr))
