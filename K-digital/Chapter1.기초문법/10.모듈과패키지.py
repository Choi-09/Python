# 1. 모듈

# (1) 모듈 import 방법 1
import theater_module as tm
tm.price(3)  # 3명이서 영화보러 갔을 때 가격
tm.price_morning(4)
tm.price_sol(5)

# (2) 모듈 import 방법 2
from theater_module import *
price(3)
price_morning(4)
price_sol(5)

# (3) 모듈 import 방법 3
from theater_module import price, price_morning
price(5)
price_morning(6)
# price_sol(4)

# (4) 모듈 import 방법 4
from theater_module import price_sol as ps
ps(5)

# ==============================================================================================

# 2. 패키지
# 모듈을 모아둔 집합. 하나의 디렉토리에 모아둔 모듈

import travel.thailand # .이하는 모듈/패키지만 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

import travel.thailand.ThailandPackage # (x)

from travel.thailand import ThailandPackage  # (o) 
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# ==============================================================================================

# 3. __all__

from travel import *  # * : __init__ 함수에서 * 의 범위를 설정해줘야 한다.  
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# ==============================================================================================

# 4. 모듈 직접 실행

from travel import *  # * : __init__ 함수에서 * 의 범위를 설정해줘야 한다.  
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

# ==============================================================================================

# 5. 패키지, 모듈 위치
# 패키지, 모듈은 현재 작성중인 python 파일과 같은 폴더에 있어야 사용가능하다.
# 해당 패키지가 어디 있는지 확인하는 코드 
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# ==============================================================================================

# 6. pip install
# pip install로 패키지 설치하기
# https://pypi.org/search/

# pip list : 현재 설치되어있는 패키지 리스트
# pip show 패키지명 : 패키지 설명
# pip install --upgrade 패키지명 : 패키지 업그레이드
# pip upinstall 패키지명 : 패키지 삭제

# ==============================================================================================

# 7. 내장함수
# https://docs.python.org/ko/3/library/functions.html
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print(f"{language}는 아주 좋은 언어입니다!")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

# ==============================================================================================

# 8. 외장함수
# https://docs.python.org/3/py-modindex.html
# glob : 경로 내의 폴더/ 파일 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))  # 현재 폴더에서 확장자가 py인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

folder = 'sample_dir'
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")
else:
    os.makedirs(folder) # 폴더생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())

import time  # 시간 관련 함수
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime # 오늘 날짜
print("오늘 날짜는", datetime.date.today())

# # timedelta: 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("오늘 부터 100일 후 날짜는: ", today + td)

# ==============================================================================================

# 9. 퀴즈
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건: 모듈 파일명은 byme.py로 작성
# (모듈 사용 예제)
# import byme
# byme.sign()

#(출력예제)
# 이 프로그램은 나도코딩 강의를 듣고 만들었습니다.
# 깃허브: https://github.com/Choi-09
# 이메일: vanessajchoi@gmail.com

import byme
byme.sig()





