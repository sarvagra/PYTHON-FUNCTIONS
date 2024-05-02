# first we need to import reduce from functools
# syntax : reduce(function,argument)

from functools import reduce 

l=[7,4,5,3,2,5]
reduce(lambda x,y : x+y , l)
#reduces a list into one entity by summing up all the numbers in the list

#we can add only upto  2 paramerters in reduce function 
# write a program to find the greatest number in a list 

l=[1,2,3,4,5,5,6,4,3,98,10]
reduce(lambda x,y : x if x>y else y , l)