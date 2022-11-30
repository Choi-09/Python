# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:20:38 2022

@author: user
"""

# csv 파일안의 문자를 숫자로 변환하기
import usecsv, re

# 1. csv파일 불러오기
total = usecsv.opencsv("popSeoul.csv")  

# 2. 파일 형식 확인(숫자로 바꿀 수 있는 원소 확인)
for i in total[:5]:
    print(i)    
 
#3. 가능하면 쉼표 지우기    
k = []
for j in i:
    if re.search('\d', j):
 #4. 정수형 or 실수형으로 바꾸기
        k.append(float(re.sub(',', '', j)))
        
    else:
        k.append(j)
        
print(k)

# case1. 숫자만 있고 자릿수 콤마가 없는 경우
# (1) csv파일 불러와서 형식 확인하기
# (2) float(), int() 함수를 통하여 문자를 숫자로 변환
n = '123'
print(float(n)) 
print(int(n))
        
# case2. 숫자만 있고 콤마가 있는 경우: re.sub() 함수로 쉼표 제거 후 float()함수 사용
j = '1,234,567'
num = float(re.sub(',', "", j))
print(num)
  
# case3. 숫자+문자로 이루어진 문자리스트 
for num1 in total:
    for num2 in num1:
        try :
            num1[num1.index(num2)] = float(re.sub(',', '', num2))
        except:
            pass
        
print("num1:",num1)