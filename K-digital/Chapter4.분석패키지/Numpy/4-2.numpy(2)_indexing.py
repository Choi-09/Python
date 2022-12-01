# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# 1. 배열의 index 접근하기================================================================
# 인덱싱(인덱스접근): 배열의 몇번재 원소의 값이 무엇인지, 특정범위의 값들이 어떤것들이 있는지 탐색하는 과정
'''
#1차원 배열
arr = np.array([1,2,3,4,5,6,7,8,9])
# arr = np.arange(10)
print(arr)

print(arr[3])   #인덱스3의 값: 4
print(arr[1])   #인덱스1의 값: 2
# print(arr[10])  # 존재하지않는인덱스값: 오류
print(arr[-1])  #뒤에서 첫번째값:9
print(arr[-3])  #뒤에서 세번째 값: 7
print(arr[-9])  #뒤에서 아홉번째 값: 1


#2차원 배열
arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr, arr.shape, arr.ndim) #ndim: 차원
print(arr[0][3] )    #행,열 순서대로
# = print(arr[0,3])

arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[3:8]) # 인덱스 3에서 8이전까지(7까지) 값
print(arr[3:])  # 인덱스 3에서 끝까지
print(arr[:7])  # 인덱스 0에서 6까지
print(arr[:-1]) # 마지막 인덱스 미만까지 출력


arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr[0, :])    # 0번째 행, 모든 열의 원소들
print(arr[:,1])     # 1번째 열, 모든 행의 원소들
print(arr[:3, :])   # 인덱스 3미만의 행, 모든 열의 원소들
print(arr[:2, 2:])  # 2번째 행 미만, 2번째 열 이상 원소
'''


#2. 배열의 Fancy 인덱싱================================================================
# 특정인덱스 여러개를 선택해서 탐색
'''
#1차원 배열

arr = np.array([5,10,15,20,25,30])
print(arr[[0,2,4]])

#2차원 배열
arr = np.array([[5,10,15],
                [20,25,30],
                [35,40,45]])
print(arr[[0,2], 2:])   # 0행과 2행의, 2열이상의 원소
print(arr[1:,[1,2]])    # 1행 이상의, 2열과 3
'''


#3. 배열의 Boolean 인덱싱===============================================================
# 불리언값을 이용해서 배열의 값을 탐색
'''
#1차원 배열
arr = np.array([1,2,3,4])
print(arr[[True, False, True, True]])     # True에 해당하는 값은 가져오고, False에 해당하는 값은 가져오지 않음

#2차원 배열
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

print(arr[[True,False,False],True])   # [[0행가져오고, 1행 안가져오고, 2행 안가져오고], 모든 열 가져오기]
'''


#4. 조건 연산자로 배열의 값 가져오기=====================================================
'''
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])


print(arr[arr>4])   #arr의 값 중 4보다 큰 원소를 전부 출력 
print(arr[arr<=9])  # arr의 값 중 9이하의 원소를 전부 출

'''


