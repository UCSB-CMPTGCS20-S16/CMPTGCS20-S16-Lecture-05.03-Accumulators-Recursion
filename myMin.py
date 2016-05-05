def myMin(someList):

    if type(someList)!=list:
        return False

    # we now know that someList is a list
    
    if someList==[]:
        return False

    # we now know that there is at least one element in the list
    # in other words: someList[0] exists!

    result = someList[0]  # initial assumption about the min

    for x in someList:
        if (x < result):
            result = x
    
    return result


