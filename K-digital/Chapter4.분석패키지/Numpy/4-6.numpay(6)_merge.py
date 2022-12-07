# 6.N차원 배열의 병합
import numpy as np
# 6-1 배열에 원소 추가 및 삭제
'''
# insert(): 리스트에 값 추가하기
arr = [1,2,3,4,5,6,7,8]
arr.insert(2,50)    #인덱스2번째에 50 추가
print(arr)

#1차원 배열
arr = np.arange(1,9)
arr = np.insert(arr, 2 ,50)
print(arr)

#2차원 배열
arr = np.arange(1,13).reshape(3,4)  # 1~12까지를 원소로 갖는 3*4 행렬만들기
arr = np.insert(arr, 2, 50, axis = 0)   # 2번째에 50 추가, axis=0이므로 행을 기준 => 2번째 행에 50추가
print(arr)

arr = np.insert(arr, 2, 50, axis =1)    #2번째에 50추가, axis=1이므로 열을 기준 =>2번째 열에 50추가
print(arr)

arr = np.insert(arr, 2, 50)     # axis값이 없는 경우 1차원 배열로 바꾼 후 2번째 열에 50넣고 출력
print(arr)

#delete(): 특정위치의 원소 삭제
arr = np.arange(1,13).reshape(3,4)
#print(arr)
# arr = np.delete(arr, 2, axis =0)    #axis=0: 행 기준, 2행삭제
# print(arr)
arr = np.delete(arr, 2,axis =1)     #axis=1: 열 기준, 2열 삭제
print(arr)

arr = np.delete(arr, 2)         #axis값을 주지 않으면 1차원 배열로 바꾼 후 인덱스2의 원소 삭제
print(arr)


#6-2. 배열간의 병합
# 두 배열을 서로 합친다.
#append() : 배열의 마지막 부분에 또다른 배열을 추가한다
arr1 = np.arange(1,13).reshape(3,4)
arr2 = np.arange(12,24).reshape(3,4)

print("arr1:\n", arr1)
print("arr2:\n", arr2)

#axis=0 : 행 기준
arr3 = np.append(arr1, arr2, axis=0)    
print("arr3:\n",arr3)

#axis=1: 열 기준
arr4 = np.append(arr1, arr2, axis=1)    
print("arr4:", arr4)

#vstack(): 행을 기준으로 열병합. (np.append(arr,arr2, axis=0)과 같다.)
arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)

print("arr4:\n", arr1)
print("arr5:\n", arr2)

arr3 = np.vstack((arr1, arr2))
print("arr6:\n",arr3)

#hstack(): 열을 기준으로 열병합
arr4 = np.hstack((arr1, arr2))
print("arr7:\n", arr4)

# concatenate() : axis값을 기준으로 두 배열 병합.(인자 나열방법이 다르다)
arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(8,14).reshape(2,3)

arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)

arr4 = np.concatenate([arr1, arr2], axis=1)
print(arr4)
'''
#6-3. 배열 분할
'''
# 2차원 배열
arr = np.arange(1,13).reshape(3,4)
print(arr)

#vsplit() : axis=0(행) 기준으로 분할
arr_vsplit = np.vsplit(arr, 3) # arr배열을 3개의 행으로 분할. arr배열의 행갯수에 따라 분할가능한 숫자가 다르다.
print(arr_vsplit)

# hsplit() : axis=1(열) 기준으로 분할
arr_hsplit = np.hsplit(arr, 2)
print("arr_hsplit:\n", arr_hsplit, "\n")

#3차원 배열 분할
arr = np.random.randint(0,10,(4,6,8))
print(arr)

arr_vsplit = np.vsplit(arr, 2) #원래 배열, 나누는 수(기존 arr 행의 수의 소인수만큼 분해가능)
print("arr_vsplit:\n", arr_vsplit)

arr_hsplit = np.hsplit(arr, 2)
print("arr_hsplit:\n", arr_hsplit)
'''















