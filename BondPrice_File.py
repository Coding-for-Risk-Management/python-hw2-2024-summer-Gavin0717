#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:25:23 2024

@author: gavin
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t = np.arange(1,ppy*m+1)
    cpn = couponRate * face
    factor = [(1+y)**(-i) for i in t]
    bondPrice = cpn * sum(factor) + factor[-1] * face
    
    return bondPrice

