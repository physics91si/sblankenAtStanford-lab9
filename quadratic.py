#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    try:
        if (a is 0) :
            raise TypeError()
    except: 
        print('a is zero')
        return
       
    print(a,b,c)
    try:
        if(not(type(a) == int and type(b) == int and type(c) == int)):
            raise TyperError()
    except:
        print('python quadratic.py physics 91si is the best')
        return
        
    mid = b**2 - 4*a*c
    try:
        if(not(mid >= 0)):
            raise TyperError()
    except:
        print('the equation has imaginary roots')
        return
    print(mid)
    sqrt_mid = mid**(1/2)
    print(sqrt_mid)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
