#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:16:44 2020

@author: imshalinshah
"""
import collections
def majorityElement(nums):
    elements = collections.Counter(nums)
    for i in nums:
        if (elements[i] >= (len(nums))/2):
            return i

print(majorityElement([3,2,3]))