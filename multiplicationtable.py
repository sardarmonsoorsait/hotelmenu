# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 02:46:10 2020

@author: smsait
"""

num=int(input("Enter the table number "))
limit=int(input("Enter the limit of table "))
count=0
while(count<limit+1):
    print(str(count) + "*" + str(num) + "  = " + str(count*num))
    count=count+1