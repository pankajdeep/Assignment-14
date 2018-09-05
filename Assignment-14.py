#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
lst=[1,2,3,4,5,6,7,8]
cube=[i**3 for i in lst]
print(cube)


#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
prime=[i for i in range(2,20) if all(i%j!=0 for j in range(2,i))]
print(prime)


#Q.3- Write the main differences between List Comprehension and Generator Expression.
The difference between list comprehension and generator expression is:
1. Syntax Differences- In list comprehension we use square brackets[] but in generator expression we use()
2. List Comprehension stores the value in form of a list but generator expression yields one item at a time
so we need to use iterator when printing items through generator expression.
3. Memory occupied by generator expression is less than that occupied through list comprehension.


#----------------------------------------LAMBDA & MAP----------------------------------------------------------------------

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
lst=list(map(lambda n:(n*1.8)+32,Celsius))
print(lst)


#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
lst=[2,3,4,5,6,7,8,9]
l=list(map(lambda a:a**2,lst))
print(l)


#--------------------------------------FILTER & REDUCE----------------------------------------------------------------------

#Q.1- Filter out all the primes from a list.
lst=[i for i in range(2,20)]
def isprime(num):
    flag=0
    for j in range(2,num):
        if(num%j==0):
            if(num==j):
                return True
            else:
                return False
        else:
            flag=1
    if(flag==1):
        return True
l=list(filter(isprime,lst))
print(l)


#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import *
lst=[i for i in range(1,5)]
r=reduce(lambda a,y:a*y,lst)
print(r)
