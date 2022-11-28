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


      5) 정규 표현식
       
    ```
     ![정규표현식](https://user-images.githubusercontent.com/51871037/204280554-2bfc2bcc-1aba-4a4f-9670-fdb9480d417e.png)
  + 2-3. 드라마 대본파일 가공

---
### 3. CSV파일로 데이터 다루기
  + 3-1. csv데이터 
  + 3-2. 파이썬으로 csv파일 읽고 쓰기
  + 3-3. csv파일 안의 문자 → 숫자 전환
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
  
