def findMissingNum(n,k):
    arrayOne = sorted(n)
    arrayTwo = sorted(k)

    for number1,number2 in zip(arrayOne,arrayTwo):
        if number1 != number2:
            print number1
        else:
            print arrayOne[-1]




# findMissingNum([7,5,4,3,2,1],[5,4,3,2,1])


def findMissingNum2(n,k):
    result = 0
    for num in n+k:
        result^=num
        # print result
    print result
findMissingNum2([1,2,3,4,5,6,7],[6,5,4,3,2,1])
