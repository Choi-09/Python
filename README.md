# Python
### start on Nov 8th 2022

+ 메소드 참고 사이트: https://docs.python.org/ko/3/library/stdtypes.html

### 1. 가상환경 설치
  * 아나콘다: https://www.anaconda.com/products/distribution
    * 파이썬과 여러가지 라이브러리를 쉽게 설치하고 관리할 수 있는 가상환경.
    * 가상환경 설치가 필요한 이유: 프로젝트 진행시 라이브러리 끼리의 충돌을 방지하기 위해서.
  * 파이썬: 아나콘다 설치시 자동설치 됨.
  
### 2. IDE 설치 
  * Spyder: https://www.spyder-ide.org/
    * 통합 개발 환경(Integrated Development Environment).
    * 코딩, 디버그, 컴파일, 배포 등 프로그램 개발에 관련된 모든 작업을 하나의 프로그램 안에서 처리하는 환경을 제공하는 소프트웨어.
    * 콘솔창에 input 가능한 기능 제공
  * colab

### 3. 한글 인코딩 오류
  1. 운영체제에 따라 한글 폰트 다르게 설정하기
주피터 노트북에서 matplotlib나 seaborn을 활용해 그래프를 그릴 때 한글 깨짐 현상 발생
운영체제에 따라 한글 폰트를 다르게 설정하여 한글 깨짐 현상을 해결

2.1. 시스템 환경 확인 및 한글 폰트 설정
platform 또는 os 모듈 : 사용자 시스템 환경 확인 - 운영체제(OS)
%config InlineBackend.figure_format = 'retina' : 레티나 설정 - 폰트 주변이 흐릿하게 보이는 것을 방지해 글씨가 좀 더 선명하게 보임
( 방법 1 ) platform
운영체제별 이름

Mac : 'Darwin'

Windows : 'Windows'

Linux : 'Linux'


( 방법 2 ) os
운영체제별 이름

Mac : 'posix'

Windows : 'nt'

Linux : 'java'(추측)

코드1 - platform

# 파이썬 시각화 패키지 불러오기
import matplotlib.pyplot as plt
%matplotlib inline


# 사용자 운영체제 확인
import platform
platform.system()
# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정


# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'

코드2 - os

# 파이썬 시각화 패키지 불러오기
import matplotlib.pyplot as plt
%matplotlib inline


# 사용자 운영체제 확인
import os
os.name
# 운영체제별 한글 폰트 설정
if os.name == 'posix': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif os.name == 'nt': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정


# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'
  * colab: https://colab.research.google.com/
    * 구글지원. 브라우저 내에서 python 스크립트를 작성하고 실행할 수 있음.
    * 직관적인 프레임으로 메모와 코드를 쉽게 추가/삭제 할 수 있음.
