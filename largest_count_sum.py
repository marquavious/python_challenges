def largest_count_sum(n):
    firstSum = 0

    for number in n:
        # sum += number
        if firstSum + number > 0:
            firstSum += number
            print "This is the number to add " + str(number)
            print "This is the sum now " + str(firstSum)
        else:
            print "its less"
    print firstSum


largest_count_sum([1,2,-1,3,4,10,10,-10,-1])
