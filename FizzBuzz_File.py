#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:55:06 2024

@author: gavin
"""
import numpy as np

def FizzBuzz(start, finish):
    fbRange = np.arange(start, finish + 1)  
    result = np.empty(fbRange.shape, dtype=object)  


    result[(fbRange % 3 == 0) & (fbRange % 5 == 0)] = "FizzBuzz"
    result[(fbRange % 3 == 0) & (fbRange % 5 != 0)] = "Fizz"
    result[(fbRange % 3 != 0) & (fbRange % 5 == 0)] = "Buzz"


    result[result == None] = fbRange[result == None]

    return result


FizzBuzz(31, 45)

