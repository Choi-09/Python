# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:41:11 2022

@author: user
"""

import csv, re
'''
# 1. read 모드로 a.csv 파일 열기
f = open("a.csv", "r", encoding=('utf-8'))

# csv파일을 저장한 객체를 파이썬에서 읽으려면 csv.reader()
new = csv.reader(f)
# print(new)

#  new안에 있는 모든 내용 출력
#for i in new:           # 커서가 맨 마지막으로 이동.
#    print(i)

#f.seek(0)      # 커서를 맨 앞으로 이동시킨다.

a_list = []  #csv형 리스트로 바꾸기 위해서 임의의 객체생성    
for i in new: 
#    print(i)                
    a_list.append(i)        # a_list에 i를 차례대로 저장

print(a_list)
'''        

# 2.  csv파일 불러오는 함수 정의 (매번 csv를 위처럼 불러오면 번거롭기때문에 라이브러리에 추가해서 import로 간편히 사용가능)
def opencsv(filename):
    f = open(filename, "r", encoding = 'utf-8')
    reader = csv.reader(f)
    output = [] 
    for i in reader:
        output.append(i)        
    return output
    f.close()


# 3. csv파일 쓰기모드로 불러오기 (with as f사용)
def writecvs(filename, the_list):
    with open(filename, "w", newline="", encoding = 'utf-8') as f:  # newline = "" : 개행을 없애준다,
                                                                    # with를 사용하면 마지막에 f.close()하지않아도 된다.
        write = csv.writer(f, delimiter = ",")  # csv리스트의 원소가 ;로 구분되어있으면 ";" 사용
        write.wirterows(the_list)


# 4. csv파일 안의 문자를 숫자로 전환하기 
def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(",", "", j))
            except:
                pass
    return listName
    