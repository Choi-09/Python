# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:48:47 2022

@author: user
"""
import numpy as np
# 4. N차원 배열 정렬
# 4-1. 1차원 배열의 정렬: 원소의 대소비교를 통해 오름차순 or 내림차순으로 정렬하는 것
'''
#오름차순 정렬
arr = np.random.randint(10, size = 10)  # 랜덤함수로 10이하의 숫자 중 임의의 정수를 뽑아 사이즈10인 1차원 배열을 만든다

print(np.sort(arr))

#내림차순 정렬
print(np.sort(arr)[::-1])  # :처음부터 :끝까지 -1씩 정렬  => 원본배열에는 정렬된 값들이 유지되지 않는 문제가 있다.

#값을 유지하면서 정렬
arr = np.sort(arr)
print(arr)
arr.sort()
print(arr)
'''

#4-2. 2차원 배열의 정렬: 
'''
arr = np.random.randint(15,size = (3,4))
#print(arr)

print(np.sort(arr)) # 기본적으로 axis=1을 기준으로 정렬(행단위로 정렬)
print(np.sort(arr, axis = 0))   #열단위로 정렬

print(np.sort(arr, axis = None))    #2차원 배열을 1차원 배열로 바꿔서 오름차순 정렬
'''
#argsort() :원소가 정렬되었을때 정렬된 원소의 원래 인덱스를 반환
'''
arr = np.random.randint(15,size = (3,4))
print("Arr:", arr)
print("sort1:", np.sort(arr, axis=1))
print("argsort1:", np.argsort(arr, axis=1))  # 원래배열이 정렬 되었을때, argsort는 일반sort배열의 원소들이 원래 배열의 어느 인덱스에 있었는지 표시. 쌍으로써야겠구만!   # axis=1: 행을 기준으로 
print("sort0:", np.sort(arr, axis=0))
print("argsort0:", np.argsort(arr, axis=0))     # axis=0: 행을 기준으로 
'''
                                           