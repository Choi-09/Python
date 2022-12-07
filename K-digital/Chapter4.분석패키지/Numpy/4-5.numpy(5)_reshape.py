#5. N차원 배열의 형태 변경  
import numpy as np  
# 5-1. 배열의 형태변경1: reshape()
'''
#1. 1차원 배열을 1+n차원 배열로 만들기
arr1 = np.arange(12)

print(arr1, arr1.ndim)  #ndim: 차원 출력
arr2 = arr1.reshape((2,6))    # 2행 6열의 2차원 배열 생성 #1차원 배열의 원소 갯수와 일치해야 한다. (3*4, 2*6, 4*3, 6*2)
print(arr2, arr2.ndim)

arr = arr1.reshape((2,3,2))
print(arr, arr.ndim)

arr4 = arr1.reshape((2,2,1,3))
print(arr4, arr4.ndim)

arr = np.arange(1,13)
print(arr)
#arr = arr.reshape(3,-1)     #reshape(3,-1)을 하면 기존 arange 한 (1,13)배열의 길이를 (1,12)로 줄이고 (3,4)배열로 만든다.
#print(arr)
#arr = arr.reshape(6,-7)
#print(arr)

arr = arr.reshape(3,2,-1)   # arange의 범위를 -1줄이고, 1~12까지의 숫자로 배열을 만든 후 3행 2열의 3차원 배열을 만든다.
print(arr)
'''
#Curse of Dimensionality: 차원의 저주: 주로 빅데이터를 다루거나 딥러닝에서 발생. 차원이 증가하면서 학습데이터수가 차원의 수보다 적어지면서 모델의 성능이 저하되는 현상
# 해결방법: 머신러닝에서 다룬다~

#5-2. 배열의 형태 변경2: resize(),ravel()
'''
arr = np.arange(12)

print(arr)
#resize(): reshape()과 비슷하지만 원본데이터를 변경시킨다는 차이가 있음
arr.resize(3,4)
print(arr)

#ravel(): 1차원 함수로 변경해준다.
arr = arr.ravel()
print(arr)
'''

# 5-3. 배열의 형태 변경3
'''
#expand_dims()  :차원 추가
arr = np.array([1,2])
print(arr, arr.shape)
# arr = np.expand_dims(arr, axis =0)  # 열을 기준으로 차원 추가
arr = np.expand_dims(arr, axis =1)  # 행을 기준으로 차원 추가
print(arr, arr.shape)

#squeeze(): 차원 줄이기
arr = np.array([[1,2]])     #1행 2열의 배열 만들기
print(arr, arr.shape, arr.ndim)
arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)

arr = np.array([[[1],
                [2],
                [3]]])
print(arr, arr.shape, arr.ndim)
arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)

arr = np.array([[[1,2,3]]])
print(arr, arr.shape, arr.ndim)
arr = np.squeeze(arr, axis =1)
print(arr, arr.shape, arr.ndim)
arr = np.squeeze(arr)   # 행렬던 텐서던 모두 1차원 배열로 차원축소한다.
'''

#5-4. 전치행렬(Transpose Matrix)
#.T : 행과 열을 전치(바꾼)한 인자를 행렬로 만든다. 데칼코마니.
'''
# 정방행렬(정사각형)
arr = np.array([[1,2,3],
                [3,4,5],
                [6,7,5]])
#print(arr, arr.ndim)
#print(arr.T)

# 정방행렬이 아닌 경우
arr = np.array([[2,3],
                [1,6],
                [7,4]])
# print(arr.T)
arr2 = np.full((3,2),3)     #3행 2열의 원소가 3으로만 이루어진 2차원 배열
print(arr2, arr2.ndim)
# print(arr.dot(arr2))        #=>오류발생! dot product연산을 하기위해서는 한 배열의 행갯수, 연산 할 배열의 열 갯수가 동일해야 한다.
print((arr.T).dot(arr2))    # 한쪽을 전치행렬 시켜주고 연산하면 된다.
'''






















