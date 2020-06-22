# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 02:10:01 2020

@author: smsait
"""

num = int(input("Enter the number of rows "))
i =0
while(i<num):
    j =0
    while(j<num-i-1):
        print(end=" ")
        j=j+1
    j=0
    while(j<i+1):
        print("*",end=" ")
        j = j+1
    i=i+1
    print("\n")
     
     