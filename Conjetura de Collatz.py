# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 20:29:07 2025

@author: Eli
"""

n = int(input())
pasos = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos += 1

print(pasos)
