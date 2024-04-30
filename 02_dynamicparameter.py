# syntax : <function name>(*parameter_name)
# take n number of inputs and stores it in a tuple
# take input , if it is an even number , stroe it in a list and print 

def even(*num):
    l1=[]
    for i in num:
        if i%2==0:
            l1.append(i)
    print(l1)
            
# syntax : <function name>(**parameter_name)
# take n number of inputs and stores it in a dictionary

def dic(**d1):
    return d1


