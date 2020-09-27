# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:29:45 2020

@author: nicol
"""



def twoSum(List, target):
#ne fonctionne pas
    A = [] 
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i] + List[j] == target:
                A.append(i)
                A.append(j)
            break       
    return A


def addTwoNumbers(l1, l2):
    n = len(l1)
    C = []
    a = 0
    b = 0
    for i in range(n):
        a += l1[i]*10**i
        b += l2[i]*10**i
    c = a + b
    for i in range(n):
        q = c//(10**(n-i-1 ))
        C.append(q)
        c -= C[i]*(10**(n-i-1 ))
    C.reverse()
    return C

import numpy as np

def lengthOfLongestSubstring(word):
    n = len(word)
    A = []
    compteur = 0
    for i in range(n):
        lettre = word[i]
        print(lettre)
        for j in range(i,0,-1):
            compteur2 = i-1
            while lettre != word[compteur2]:
                compteur  += 1
                compteur2 -= 1
        A.append(compteur)
    return A
 
def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums = np.sort(nums)
    nums = np.median(nums)
    return nums
        
    