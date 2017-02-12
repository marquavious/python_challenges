#
n = [-1,5,4,3]
#
def findSum(n,k):
    coupleCout = 0
    iterationCount = 0
    curentMatches = []
    seen = set()

    while iterationCount <= len(n):
        for num in n:
            index = 0
            print iterationCount
            a = n[index]
            index += 1
            if a+num == k:
                print "match"
                seen.add((a,k))
                coupleCout += 1
            print "no match"
            iterationCount += 1
    print curentMatches
    print coupleCout

findSum(n,4)


def pair_sum(arr,k):

    if len(arr)<2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k-num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )


    # FOR TESTING
    print len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

# pair_sum(n,4)
