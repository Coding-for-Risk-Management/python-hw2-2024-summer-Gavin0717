#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:41:04 2024

@author: gavin
"""
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    
    cpn = couponRate * face
    t = np.arange(1,m*ppy+1)
    pvcf = [cpn*(1+y)**(-i) for i in t]
    pvcf[-1] += face * (1+y)**(-m*ppy)
    pvcf_t = [i*cpn*(1+y)**(-i) for i in t]
    pvcf_t[-1] += m*ppy*face * (1+y)**(-m*ppy)
    bondDuration = sum(pvcf_t)/sum(pvcf) 
    
    
   
    return bondDuration



# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1