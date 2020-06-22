# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:33:15 2020

@author: smsait
"""
print ('*******MENU******\n')
print (' 1 - Biriyani \n 2 - Borrotta \n 3 - Friedrice \n 4 - Mandhi \n')
item = int(input ('Enter the number for corresponding item  ' ))
if item == 1:
    print('your order is Biriyani ,Please wait few minutes')
elif item == 2:
    print('your order is Borrotta ,Please wait few minutes')
elif item == 3:
    print('your order is friedrice ,Please wait few minutes')
elif item == 4:
    print('your order is Mandhi ,Please wait few minutes')
else:
    print('you are enter unvalid number ,Please order again')