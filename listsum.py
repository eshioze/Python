# This function takes a list of numbers as argument and validates that the argument is indeed a list and return the sum of the items in the list
def listsum():
   aList = [45,3,7,5,8,2.5]
   print('This is the list below')
   print(aList)
   print('The sum of the list is:')
   sum(i for i in aList)
   print(sum(aList))
listsum()