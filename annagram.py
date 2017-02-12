
# def ann(n,k):
#     n = n.replace(' ','')
#     k = k.replace(' ','')
#     finalCount = len(n) #Could be k
#     placeHolderCount = 0
#
#     if len(n) == len(k):
#         index = 0
#         for letter in k:
#             if letter == n[index]:
#                 # print "this is the k index" + k[index]
#                 print "Comparing: " + letter + " and " + n[index]
#                 print "THE LETTERS MATCH!!"
#                 index += 1
#                 placeHolderCount += 1
#             else:
#                 print "Comparing: " + letter + " and " + n[index]
#                 print "THE LETTERS DO NOT MATCH!!"
#                 index += 1
#                 placeHolderCount -= 1
#
#
#     if placeHolderCount != finalCount:
#         print finalCount
#         print "Not an annagram"
#     else:
#         print "It is an annagram"
#
# ann("dog","god")

def anagram(s1,s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)
