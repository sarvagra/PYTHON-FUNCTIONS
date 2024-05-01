# a generator function generates an iterator object 

#write a program for generator function for extractin even numbers from a list.

def eve(*num):
    l1=[]
    for i in num:
         if i%2==0:
            yield i
    