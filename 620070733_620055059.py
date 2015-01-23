import itertools

def digits(x):
    def helper(x,result): 
        if x/10<1:#checks if x has 1 digit
            return result
        else:
                return helper(x/10,result+1)##while the number divided b 10 has more than one digits then helper is incrimented 
    return helper(x,1)# initialises result at 1

##2 this can be done multiple ways and i did both ways...description in the 2nd lcs
def lcs(y):
    x=list(int(y) for y in str(y))
    a=x.pop(0)
    x.append(a)
    k=[str(i) for i in x]
    return int(''.join(itertools.chain.from_iterable(k)))

def LCS_2(x):
    z='' #initialises z as a String
    y=list(int (x) for x in str(x)) #converts te integers into a list of individual ints
    popped=y.pop(0)#removes the first element in the list...which is the first digit of the number
    y.append(popped)#appends the first digit that was removed to the end of the list
    stringed=[str(x) for x in y]#turns each integer into a string
    for i in stringed: # i takes the value of each string in the list
        z+=i ##concatenates the elements in the list with the first digit now at the end of the number
    return z
        
       
    
def isprime(n):
    if n>1: # evaluates the preceeding statments if n is greater than 1
        for x in range(2,n):# x takes on the value of the integers from 2-n
            if n%x==0:#checks if n is divisible by any integer before it
                return False
        return True
    else:
        return False #if n is less than 1 then the program returns False

    
def isCircular(x):
    def helper(x,dgs):
        if isprime(x) and dgs<=1:##checks if the number that is inputted is a prime and if the number of digit it has is less than or equal to 1
                return True
        elif not isprime(x):#if the number is not prime a value of false is returned
            return False
        else:
            return helper(lcs(x),dgs-1) # the helper function applies the lcs function written above to the number x and minuses 1 from digits 
    return helper(x,digits(x))# checks the amount of digits in the integer x
       
        
        
def nbrCirPrimes(x):
    lis=[] #lis is initialised as an empty list
    for i in range(2,x):
        if isCircular(i) and isprime(i):
            lis+=[i]
    return len(lis)
        
def fac(x):
    def helpme(x,r):
        if x==1:
            return r
        else:
            return helpme(x-1,r*x)
    return helpme(x,1)





















       
    
       
        
    

