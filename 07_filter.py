# filters out the required data
# syntax : filter (function,argument)

# using filter function to filter out even numbers from a list

l=[2,3,4,5,6,7,8,9,10,12,13,19,17,14]
list(filter(lambda x : x%2==0 , l))
