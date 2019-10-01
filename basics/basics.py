# This is a comment
def getMax(aList):
    max = aList[0]
    for number in aList:
        if number > max:
            max = number
    return max
arr = [-5, -2, -4, -6, -3]
print("Max: "+ str(getMax(arr)))