## Python 정리

### 목차:
1. [기초문법](#1.-기초-문법)
2. [텍스트 파일 가공](#2.-텍스트-파일-가공)
3. [CSV파일로 데이터 다루기](#3.-CSV파일로-데이터-다루기)
4. [다양한 패키지로 데이터 분석](#4.-데이터분석)
5. [웹크롤링](#5.-웹크롤링)
  
---
### 1. 기초 문법
  + 1-1. 기본연산자
     +  (1)
  + 1-2. for
  + 1-3. def
  + 1-4. input
  + 1-5. if-else

---
### 2. 텍스트 파일 가공
  + 2-1. 파일 입출력 연습
    ```
    1) 텍스트 파일 생성 및 내용 입력
      • 파일 입출력 명령어: w(rite), r(ead), a(ppend)
      • f.close() 해야 저장하고 닫힌다.
      • with문을 사용하면 자동으로 close가 된다.
         >> with open("파일명.txt", "w") as f:
              f.write("내용")
              
              
    2) 명령어
      - 파일생성, 내용입력
        •  f = open("파일명.txt","w")    // 파일생성
              f.wrtie("내용")     // 내용입력
      
      - 파일 읽기
        • f = open("파일명.txt", "r")    // 파일 읽기
          res = f.read()        
          print(res)    // print() 함수를 써야 내용이 보이기 때문에 res변수에 넣고 출력해준다.
          f.close() 
       
      - 내용 추가
        • f = open("파일명.txt", "a")    // 내용 추가
            f.write( "추가할 내용")
    ```            
            
  + 2-2. 정규표현식으로 문자열 가공
    ```   
    1) 긴 문자열에서 원하는 형태의 문자열 찾기 위해 사용


    2) 모듈 임포트
      - import re   // 정규식 일치 연산을 제공하는 모듈


    3) 메서드
      - match() : 문자열의 도입부분이 매치되는지 체크 (중간부가 일치하면 찾을수 없다.)
        • re.match(패턴, 문자열)
          ex) >>> pattern = r'life'
              >>> script = 'life is so cool'    // (O) ==> 'It is a cool life' (X)
              >>> re.match(pattern, script)
              >>> re.match(pattern, script).group()  
              or
              >>> re.match(r'life', 'life is so cool').group()

      - search() : 모든 구간의 선두에 한해서 매치하는지를 체크, 추출 
        • re.search(패턴, 문자열)
          ex) >>> pattern = r'life'
              >>> script = 'It is a cool life'    // (O)

      - fullmatch() : 문자열 전부가 매치되는가를 체크 

      - findall() : 매치된 부분 모두 리스트로 출력. 찾지 못하면 오류가 아니라 빈리스트 반환.
        • re.findall(패턴, 찾으려는 문자열)
          ex) >>> e = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
              >>> re.findall(r'\d.+년', e)   //~년이 들어가는 문자열을 모두 찾지만 '에', '에는', '입니다' 같은 불필요한 데이터도 함께 출력된다.(탐욕)
              ['91년에 태어났습니다.', '97년에는 IMF가 있었습니다.', '2020년입니다.']

      - finditer() : 매치된 부분 모두 이터레이터(iterator)로 취득 

      - sub() subn() : 매치된 부분을 치환 

      - spilt() : 정규표현 패턴으로 문자열을 분할 
        • re.split(패턴, 문자열)
          ex) >>> sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
              >>> re.split(r'[.?!]', sentence)
              ['I love a lovely dog really', 'I am not telling a lie', 'What a pretty dog', 'I love this dog']


    4) 탐욕제어
        - 불필요한 데이터까지 모두 매칭 시켜버리는 오류를 수정.
        • ? 
        ex) >>> e = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
            >>> re.findall(r'\d.+?년', e)
            ['91년', '97년', '2020년']


    5) 정규 표현식(하단 표)     
    ```
       ![정규식 메타문자](https://user-images.githubusercontent.com/51871037/204778769-edc25817-8928-49ad-807c-4d9126817039.PNG)


  + 2-3. 드라마 대본파일 가공
    ```
    1) ide에서 파일 열기
        - 가공하려는 텍스트파일을 py 저장소와 같은 폴더에 저장 
           or 'import os' → os.chdir(r'경로')

        - 파일 열어서 확인
          • f = open('friends101.txt', 'r' )

        - read한 파일을 출력하기 위해서 변수에 저장
          • s101 = f.read()

        - 콘솔에 출력해서 내용 확인
          • print(s101)

     2) 작업
         (1) 정규표현식으로 원하는 정보 추출하기
         (2) 빈 객체 생성: 문자열(""), 배열([]) 등
         (3) 객체에 원소 추가 (for문)
         (4) 새로운 파일 만들어서 열기: 변수명 = open('파일명.확장자', 'w/r/a')
         (5) 새로운 파일에 객체 원소 넣기: 변수명.writelines(객체명)  //usecsv에서 writelines를 정의해놓았기때문에 가능
         (6) 파일 닫으며 저장: 변수명.close()

         - 모니카 라인 찾기             
         - 등장인물 찾기 (1)
         - 등장인물 찾기(2): 모든 명령어를 한줄로 입력하기
         - 괄호 안의 문자열만 검색
         - 특정 단어가 포함된 문자열 찾기
     ```
---
### 3. CSV파일로 데이터 다루기
  + 3-1. csv데이터 
    ```
    1) csv파일 만들고 읽기
       - csv란?: 쉼표로 나눠진 값을 저장한 데이터. 엑셀에서도 활용가능, 파이썬으로 불러와 복잡한 연산 수행 가능
       - 파일만들기: (1) 엑셀의 A1열부터 데이터를 작성한다. 저장시 .csv 파일 형식으로 저장
                    (2) 메모장에서도 작성 가능. 제일 첫째줄에 컬럼명을 쉼표로 구분해서 적고 다음 행에 값을 적어 csv파일형식으로 저장
    ```
    
  + 3-2. 파이썬으로 csv파일 읽고 쓰기
    ```
    1) csv파일 읽기
       - csv파일 경로로 이동
         • import os
           os.chdir(r'경로')

       - csv파일 읽기모드로 열기
         • import csv
           f = open("파일명", "r")   // 한글파일이 열리지 않으면 encoding = 'utf8'
       
       - csv.reader()로 csv파일 내용 읽기
         • new = csv.reader(f)    // 객체f를 csv.reader로 읽어 new라는 객체에 저장

       - 읽은 csv파일을 csv형 리스트로 저장하기(csv파일을 파이썬에서 사용할 수 있도록)
         •  list = []    // csv형 리스트로 바꾸기 위해서 임의의 객체 생성
            for i in list:
               print(i)
               list.append(i)    // list에 i를 한 행씩 차례대로 저장
            print(list)    
              
     2) csv파일 쓰기
        - csv형 리스트 만들고 객체에 저장
          • 변수명 = [['컬럼1', '컬럼2', '컬럼3', '컬럼4',..., '컬럼n']]
          
        - 파일을 쓰기(w) 모드로 생성해 객체에 저장
          • f = open('파일명', 'w', newline = '')  
          
        - 파일을 생성한 객체에 csv.writer()를 사용해 csv객체 열기
          • csvobject = csv.writer(f, delimiter = ',')    // csv형 리스트 원소가 ;로 구분되어 있으면 delimiter=';'사용
          
        - writerows()로 csv형 리스트를 쓰고 
          • csvobject.writerows(변수명)
          
        - close()로 파일 저장 후 닫기
          • f.close()
    ```
      + csv파일 읽기, 쓰기, (숫자로)전환하기 라이브러리
         ```
         (1) opencsv 
             • def opencsv(filename):
                  f = open("파일명", "r)
                  reader = csv.reader(f)
                  output = []
                  for i in reader:
                     output.append(i)
                  return output
              * 읽을때: opencsv("파일명")  

         (2) writecsv
             • def writecsv(filename, the_list):    // filename: 만들 파일이름, the_list: csv형 리스트 저장객체
                  with open(filename, "w", newline = '') as f:    // with문으로 자동close.
                      a = csv.writer(f, delimiter = ',')
                      a.writerows(the_list)
                      
          (3) switchcsv
              •
          ```
                      
  + 3-3. csv파일 안의 문자 → 숫자 전환
    ```
    (1)
    ```
  + 3-4. csv파일 데이터 분석

---
### 4. 데이터분석
  + 4-1. 분석 패키지 설치
  + 4-2. 넘파이 : 배열
  + 4-3. 넘파이: 사업성 분석
  + 4-4. 판다스 : 데이터프레임 
  + 4-5. 판다스 : 통계 데이터
  + 4-6. 실전 통계분석
  + 4-7. 맷플롯립 : 그래프 그리기

---
### 5. 웹크롤링
  + 5-1. 웹크롤링이란
  + 5-2. 웹크롤링 준비
  + 5-3. 포털사이트에서 기사 크롤링
  + 5-4. 프로그램 실행파일 만들기

---
<End>
  
