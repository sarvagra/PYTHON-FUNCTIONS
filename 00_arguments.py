# syntax : def <name>(argument) 
# this code takes input from user and stores it in the variable 'l'
# create a function to separate numbers from a list and display them as anotheer list

def ext(l):
    l2=[]
    for i in l :
        if type(i)==int or type(i)==float:
            l2.append(i)
 
    print(l)
    print("EXTRACTED NUBER LIST :",l2)


    
# write a program to join two lists
  
def conct(l1,l2):
    return (l1+12)

