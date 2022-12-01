# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:13:06 2022

@author: user
"""

import usecsv,re   #lib에 저장한 usecsv라이브러리 불러오기  

pop = usecsv.opencsv("popSeoul.csv")    # usecsv의 opencsv메소드를 이용해 popSeoul.csv파일 열기
#print(pop[:4])


newPop = usecsv.switch(pop)    # usecsv에 저장한 switch 메소드를 이용해 문자를 숫자로 전환
#print(pop[:4])

# print(i)

'''
newPop리스트 확인하기 
# 외국인의 비율: 리스트의 두번째(외국인수) / (리스트첫번째(한국인) + 리스트의 두번째(외국인수))
for i in newPop:    # newPop의 리스트 i 
    try:
        f = round((i[2] / (i[1]+i[2]) * 100) ,1)    
        print(f"구이름:{i[0]}\t\t외국인 비율{f}")
    except:
        pass
'''

new = [['구', '한국인', '외국인', '외국인 비율(%)']]    # 배열이 하나의 행. 배열안에 배열로 넣어줘야 한 행으로 묶인다.
for i in newPop:
    try:
        f = round((i[2] / (i[1]+i[2]) * 100) ,1)    
        if f > 3:
            new.append([i[0], i[1], i[2], f])   # f가 3보다 크면 각 컬럼 값을 리스트로 추가한다.
    except:
        pass

usecsv.writecsv("newPop.csv", new)  # append한 값을 newPop.csv파일로 생성.

