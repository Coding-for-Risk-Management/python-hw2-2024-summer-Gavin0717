#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:55:06 2024

@author: gavin
"""
import numpy as np

def FizzBuzz(start, finish):
    
    fbRange = np.arange(start, finish + 1)
    
    result = fbRange.astype(str)
    
    result = np.where((fbRange % 3 == 0) & (fbRange % 5 == 0), "fizzbuzz", result)
   
    result = np.where((fbRange % 3 == 0) & (fbRange % 5 != 0), "fizz", result)

    result = np.where((fbRange % 3 != 0) & (fbRange % 5 == 0), "buzz", result)
    

    return result


print(FizzBuzz(31, 45))

