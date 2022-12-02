# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:31:54 2022

@author: user
"""
import numpy as np

#N차원 배열 연산 : N차원배열 연산을 위해서는 두 배열의 shape이 같아야 한다.

#1. 배열의 연산1: 사칙연산/제곱/제곱근/몫/나머지
'''
arr1= np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

arr2 = np.array([[2,2,2],
                 [2,2,2],
                 [2,2,2]])

#덧셈
print(arr1 + arr2)
#(=) print(np.add(arr1, arr2))

#뺄셈
print(arr1-arr2)
#(=)print(np.subtract(arr1,arr2))

#곱셈 : 행렬간의 내적 연산이 아닌 단순 원소단위의 곱
print(arr1*arr2)
print(np.multiply(arr1, arr2))

#나눗셈
print(arr1/arr2)
print(np.divide(arr1,arr2))


# 제곱연산
print(arr1 ** 5)
print(np.square(arr1))


#제곱근
print(np.sqrt(arr1))

#몫
print(arr1//2)


#나머지
print(arr1 % 2)
'''

#2. 배열의 연산2: 내적(dot product)/절댓값/올림/내림/반올림/버림
'''
#2-1. 1차원행렬의 닷프로덕트: 각원소의 곱의 합 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.dot(arr1,arr2))
'''
#2-2. 2차원행렬의 닷프로덕트
'''
[[a,b],     [[e,f],         [[ae+ ag, af+bh]
 [c,d]]      [g,h]]]  =>     [ce + dg, cf+dh]]
'''
'''
arr1 = np.array([[1,2],
                 [4,5]])
arr2 = np.array([[1,2],
                 [0,3]])

print(np.dot(arr1,arr2))

#절댓값
arr1 = np.array([[-1,2],
                 [4,-5]])

print(np.abs(arr1))

#올림연산
arr1 = np.array([[-1.9332,2.412],
                 [4.131,-5.845]])
print(np.ceil(arr1))


#내림연산
print(np.floor(arr1))

#반올림 연산
print(np.round(arr1))

#버림 연산
print(np.trunc(arr1))
'''


#3. 배열의 연산3: min/max/sum/mean/std/cumsum/median
'''
arr1 = np.array([[1,2,3],
                 [4,5,8]])

# 최솟값: min()
print(np.min(arr1))
print(arr1.min())
print(arr1.min(axis=1))     # axis=1 : 0행 가장 작은 원소, 1행 가장 작은 원소 반환
print(arr1.min(axis=0))     # axis=0 : 0열 중 가장 작은원소,  1열 중 가장 작은원소, 2열 중 가장 작은 원소 반환 


#최댓값: max()
print(np.max(arr1))
print(arr1.max(axis = 0))    # axis=0 : 0열 중 가장 큰원소,  1열 가장 큰 원소, 2열 가장 큰 원소 반환
print(arr1.max(axis = 1))    # axis=1 : 0행 가장 작은 원소, 1행 가장 작은 원소 반환
 

#sum()
print(np.sum(arr1))
print(arr1.sum(axis = 0))   #axis=0 : 각 열의 합
print(arr1.sum(axis=1))     #axis=1 : 각 행의 합


# 원소들의 평균값: mean()
print(np.mean(arr1))
print(arr1.mean(axis=0))    # axis=0 : 각 열의 평균
print(arr1.mean(axis=1))     # axis=1 : 각 행의 평균


# 표준편차: std()
print(np.std(arr1))
print(arr1.std(axis=0))     #axis=0 : 각 열의 표준편차
print(arr1.std(axis=1))     #axis=1 : 각 행의 표준편차


# 누적값: cumsum() : 각원소의 누적값을 출력
print(np.cumsum(arr1))
print(arr1.cumsum())    #1차원 배열로 출력
print(arr1.cumsum(axis=0))  # axis=0 : 0행을 기준으로 누적값 계산. 0행은 그대로 출력, 1행의 원소와 0행의 원소의 누적값을 1행으로 출력 
print(arr1.cumsum(axis=1))  # axis=1 : 1열을 기준으로 누적값 계산. 1열은 그대로 출력, 2열,3열에 누적값 출력 

 
# 중앙값: median() : 원소의 가장 가운데값. 원소가 짝수개일경우 중간 2개의 평균값이 중앙값
print(np.median(arr1))      # 3,4의 중앙값

arr1 = np.array([[1,2,3],
                 [4,5,8],
                 [7,3,5]])
print(np.median(arr1, axis=0))  #axis=0: 각 열의 중앙값 출력
print(np.median(arr1, axis=1))  #axis=1: 각 행의 중앙값 출력
'''

#4. 배열의 연산4: 비교연산/ 삼각 함수
'''
#4-1. 비교연산: 
arr1 = np.array([[1,2,3],
                 [4,5,6]])

arr2 = np.array([[2,6,1],
                 [5,7,5]])

#print(arr1 == arr2)    # 같은 위치에 있는 각 원소들의 값이 같으면 True, 다르면 False를 출력 

# print(arr1>arr2) # 같은 위치에 있는 원소들의 대소비교 후 arr1의 원소가 크면 True, 작으면 False 출력 

#print(np.array_equal(arr1,arr2)) #배열전체가 같은지 확인

# 4-2. 삼각함수
arr1 = np.array([[1,2,3],
                 [4,5,6]])

#sin()
print(np.sin(arr1))

#cos()
print(np.cos(arr1))

#tan()
print(np.tan(arr1))

#pi
print(np.pi)

a = 2
print(a*np.pi)
'''
# 5. 브로드캐스팅(BroadCasting) : 기존의 배열 연산은 배열들의 shape이 같아야 하는 번거로움이 있었는데 브로드캐스팅을 적용하면 안그래도 됨.
#브로드캐스팅 적용하면 서로의 배열shape을 연산이 가능하도록 자동으로 맞춰 연산한다.
'''
#ex1)
arr1 = np.array([[0,0,0],
                 [1,1,1],
                 [2,2,2]])
arr2 = np.array([[5,6,7]])

print(arr1+arr2)

#ex2)
arr1 = np.array([[2,2,2]])
arr2 = np.array([[5],
                 [7]])
print(arr1+arr2)
'''

#6. 벡터(행렬) 연산의 장점: 처리 속도가 빠르다!
# 딥러닝 선형대수관련 연산 처리 시 처리속도가 빠름
import time  #시간계산 패키지
'''
arr = np.arange(9999999)
#for문
sum = 0;
before = time.time()
for i in arr:
    sum+= i
after = time.time()
print(sum, after-before, "초")


# 벡터 연산
before = time.time()
sum = np.sum(arr)
after = time.time()
print(sum, after-before, "초")
'''

arr1=np.arange(9999999)
arr2=np.arange(9999999)

#for
'''
sum = 0
before = time.time()
for i, j in zip(arr1, arr2):    #zip: 갯수가 동일한 자료를 묶는 함수
    sum += i*j
after = time.time()
print(sum, after - before, "초")


#벡터 연산
before = time.time()
sum = np.dot(arr1, arr2)
after = time.time()
print(sum, after-before, "초")
'''






























































