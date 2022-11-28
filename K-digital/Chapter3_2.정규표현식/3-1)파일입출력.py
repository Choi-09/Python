# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:50:14 2022

@author: user
"""

"""3-1. 파일 입출력 연습하기

1) 텍스트 파일 생성 및 내용입력.
*   파일 입출력 명령어: w(rite), r(ead), a(ppend)
*   f.close() 로 닫아준다.

2) 명령어
*  f = open("test.txt","w")  : 내용입력

    f.wirte("내용")   
*  f = open("test.txt", "r") : 파일 읽기

    res = f.read()   
          
    print(res)

    f.close()         
          # print() 함수를 써야 내용이 보이기 때문에 res변수에 넣고 출력해준다.

*  f = open("test.txt", "a") : 내용추가

    f.write("append하기")
"""

import os

f = open("test.txt","w")
f.write("파일내에 저장\n")
f.write("파일내에 저장2")
f.close()

# w(rite),r(ead),a(ppend) 3가지

f = open("test.txt", "r")
res = f.read()
print(res)
f.close()

f = open("test.txt", "a")
f.write("append하기")
print(res)
f.close()

from google.colab import drive
drive.mount('/content/drive')

with open("test.txt", "w") as f:
  f.write("파일에 저장")
# with문을 사용하면 자동으로 close가 된다.

print("1. 새로운 메모장\n", "2. 메모장 보기\n", "3. 메모 추가\n")
while True :
  choice = int(input("명령을 선택하세요 >>"))
  
  if choice == 1:
    print("새로운 메모장을 생성합니다.\n")
    memo = input( "메모입력:")
    with open("test.txt", "w") as f:
         f.write(f"{memo}\n")
  elif choice == 2:
    print("메모장 보기")
    with open("test.txt", "r") as f:
      for line in f:  # 메모장 한줄씩 보기(방금 추가한 내용이 보인다.)
        print(line, end="\n")
      # print(f.read())
  elif choice == 3:
    print("메모장에 내용 추가")
    memo = input("내용을 추가 해 주세요")
    with open("test.txt", "a") as f:
      print(f.write(f"{memo}\n"))
  else:
    print("종료합니다.")
    break