# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 16:57:01 2022

@author: user
"""

import usecsv, re

apt = usecsv.opencsv("apt_202211.csv")  # csv파일 열기
newApt = usecsv.switch(apt)     # 파일 열고, 문자를 숫자로 전환하여 newApt변수에 넣는다
# print(newApt[:4])
'''
GangWon = [['시군구','단지명','전용면적(㎡)','거래금액(만)']]   
for i in newApt:
    try:
        if i[5] >= 120 and i[8] <=30000 and re.match(r'강원',i[0]):
           # print(f"{i[0]}| {i[4]}| {i[8]}| {i[5]:2}")
           GangWon.append([i[0], i[4], i[8], i[5]])
    except:
        pass

usecsv.writecsv("GangWon.csv", GangWon)
'''

Busan = [['시군구','단지명','전용면적(㎡)','거래금액(만)', '건축연도']] 
for i in newApt:
    try:
        if i[5] <=100  and i[8] <=50000 and re.match(r'부산',i[0]) and i[10]>=2017:
           # print(f"{i[0]}| {i[4]}| {i[8]}| {i[5]:2}")
           Busan.append([i[0], i[4], i[8], i[5], i[10]])
    except:
        pass

usecsv.writecsv("Busan.csv", Busan)