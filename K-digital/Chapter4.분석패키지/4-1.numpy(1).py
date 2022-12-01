# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:03:00 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt

'''
# 1. N차원 배열 생성
## n차원 배열 생성=================================================================================
### 1차원 배열
arr = np.array([1,2,3])
print(arr)

###2차원 배열
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#리스트와 구분!
print(type([1,2,3]))
print(type(arr))

### list와 튜플로 n차원 배열 만들기
tpl = (4,5,6)
arr = np.array(tpl)
print(arr)

list = [1,2,3]
arr = np.array(list)
print(arr)

list2 = [[1,2,3], [4,5,6]]
arr = np.array(list2)
print(arr)

### shape: 배열모양
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr1.shape, arr.shape)    #arr1.shape: 원소가 3개인 1차원 배열   # arr2.shape: 행이2개이고 열이 3개인 2차원 배열

#### ndim : 차원
print(arr1.ndim, arr2.ndim)

### size: 사이즈
print(arr1.size, arr2.size)



## n차원 배열의 데이터 타입 =========================================================================

### array의 데이터 타입 정의하기
arr = np.array([1.1,2.2,3.3], dtype=np.int)
print(arr, arr.dtype)

arr = np.array([0,1,1], dtype=np.bool)
print(arr, arr.dtype)

arr = arr.astype(np.float32)
print(arr, arr.dtype)

### 데이터 타입이 흔재하는 경우
#(1) int, float타입 혼재
arr = np.array([1,2,3.4])   # 배열의 원소가 int, float 혼재
print(arr, arr.dtype)       # float 타입으로 출력

#(2) string숫자, 숫자 타입 혼재
arr = np.array([1,2,3.4,"4"], dtype = int)    # 스트링타입의 "4"가 int로 전환된다.
print(arr,arr.dtype)

#(3) string문자열, 숫자 혼재
 arr = np.array([1,2,3.4,"문자열"], dtype = int)   # 숫자로 바꿀 수 없는 문자열은 배열에 넣을 수 없다!
 print(arr, arr.dtype)


## 정해진 형식의 N차원 배열 생성하기 ====================================================================

### np.zeros(): 모든 원소가 0인 배열 생성
arr = np.zeros([2,2])   #함수의 인자는 배열의 shape
print(arr)

### np.ones() : 모든 원소가 1인 배열 생성
arr = np.ones([3,1])
print(arr)

### np.full(): 모든원가 지정된(fill value) 원소가 있는 배열 생성
arr = np.full([2,3], 5) # shape, value 가 인자.
print(arr)

### np.eye(): 행을 n, 열을 m 이라고 했을 때 대각원소가 1이고 나머지 0인 n*m배열 생성
arr = np.eye(3)   #k: 대각원소의 발생지점을 어느부분으로 할 지. 보통 k=0으로 고정, n만 적어주면 정방형 배열 생성
print(arr)


### 지정된 배열과 똑같은 크기의 배열 만들기
arr = np.array([[1,2,3], [4,5,6]])

#(1) np.zeros_like()
arr_z = np.zeros_like(arr)
print(arr_z)

#(2) np.ones_like()
arr_o = np.ones_like(arr)
print(arr_o)

#(3) np.full_like()
arr_f = np.full_like(arr, 3)
print(arr_f)


## 특정 범위의 값을 갖는 N차원 배열 생성하기 ==========================================================
### np.arange(): 순차적으로 나열
lst = list(range(0,9,2))
print(lst)

arr = np.arange(9)  # stop 9
print(arr)
arr = np.arange(3,12)   # star from 3, stop before 12
print(arr)
arr = np.arange(3,12,3)     # start from 3, stop before 12, step 3
print(arr)

arr = np.arange(stop = 9, step = 2, start = 0)
print(arr)

### np.linspace() : start, stop값은 동일 (arange와 유사하지만 차이있음!)
arr = np.linspace(0, 100, 11) #0부터 100 이하(포함!!)의 숫자 중 11개의 원소를 균등한 간격으로 배열에 넣음
print(arr)

### np.logspace(): 로그값 스케일의 린스페이스메소드. 지정된 범위에서 num갯수만큼 균든한 간격으로 log 단위대로 n차원 배열에 넣음
arr = np.linspace(1,10,10)
print(arr, end = "\n\n")

arr = np.logspace(1,10,10, base = 2)
print(arr)

arr = np.logspace(1,10,10)      #linspace를 logspace의 인자로 지정하지 않으면 상용로그 스케일로 원소가 출력
print(arr)


## 난수로 이루어진 N차원 배열 생성하기 =================================================================

### 데이터를 시각화 할 수 있는 맷플롯립이라는 라이브러리 사용
import matplotlib.pyplot as plt

### np.random.normal(): 정규분포의 확률 밀도에서 표본 추출
arr = np.random.normal(0,1,(2,3))    # 인자: 정규분포의 평균, 표준편차, 추출할 갯수/행렬사이즈
print(arr)

arr = np.random.normal(0,1,100000)
plt.hist(arr, bins=100)
plt.show()

#npm.random.rand(): 0에서1사이의 값을 균등한 비율로 표본추출
arr= np.random.rand(1000)   # 인자: 표본갯수
plt.hist(arr, bins = 100)
plt.show()

#np.random.randn(): -1부터 1 사이의 값을 정규분포(가우시안분포)의 표본을 추출
arr = np.random.randn(1000)     # 인자: 표본갯수
plt.hist(arr, bins=100)
plt.show()

#np.rand.int(): 랜덤한 정수만 출력
arr = np.random.randint(low = 1, high = 5, size = (3,4))    #1부터 5미만까지 10사이즈의 배열 생성. low값 없으면 자동hgih 값으로 인, 0부터 high까지 랜덤수 추출.
print(arr)


arr = np.random.randint(100,200,1000)
plt.hist(arr, bins =100)
plt.show()


## 시드(seed)값을 통한 난수 생성 제어=======================================================================

arr = np.random.rand(10)
print("난수 발생\n", arr)

arr = np.random.rand(10)
print("난수 발생\n", arr)

#seed값으로 시작값을 고정. 시작값이 같으면 같은 난수값 추출. 
np.random.seed(1)   #반드시 시작값 지정!
arr = np.random.rand(10)
print("난수발생1\n", arr)

np.random.seed(1)   #같은 난수추출원하는 곳에도 같은 시작값 지정!
arr = np.random.rand(10)
print("난수발생2\n", arr)
'''



















