# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 02:07:09 2019

@author: Sourav Banerjee
"""

def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = 20
# Driver Code (Note that lst is not modified 
# after function call. 
x = 10 
myFun(x); 
print(x) 
#########################
def myFun(x): 
   x[0] = 20
  
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst) 