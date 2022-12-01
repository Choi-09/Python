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
