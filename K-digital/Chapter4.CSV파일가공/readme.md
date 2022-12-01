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
         >>> py 파일로 저장 후 python 폴더 > Lib에 저장
         (1) opencsv 
             • def opencsv(filename):
                  f = open("파일명", "r)
                  reader = csv.reader(f)
                  output = []
                  for i in reader:
                     output.append(i)
                  return output
              * 읽을때: .opencsv("파일명")  

         (2) writecsv
             • def writecsv(filename, the_list):    // filename: 만들 파일이름, the_list: csv형 리스트 저장객체
                  with open(filename, "w", newline = '') as f:    // with문으로 자동close.
                      a = csv.writer(f, delimiter = ',')
                      a.writerows(the_list)
               * 쓸때: .writecsv("파일명", csv형리스트 객체명)       
                 
          (3) switchcsv
              • def switch(listName):
                  for i in listName:
                      for j in i:
                          try:
                             i[i.index[j]] = float(re.sub(',', '', j))
                          except:
                             pass
                  return listName 
                * 바꿀때: .switch(opencsv변수명) 
          ```
                      
  + 3-3. csv파일 안의 문자 → 숫자 전환
    ```
    (1) 숫자만 있고 자릿수 콤마가 없는 경우
        ex) >>> n = '123456'
            >>> print(float(n))
                (or) print(int(n))
    
    (2) 숫자만 있고 자릿수 콤마가 있는 경우: re.sub() 함수로 쉼표 제거 후 float()함수 사용
        ex) >>> j = '1,234,567'
            >>> k = float(re.sub(',', "", j))
            >>> print(k)
          
    (3) 문자형 숫자만 골라서 숫자형으로 바꾸기
        ex) p = ['123강남', '151,767', '11,093', '27,397']
            k = []
            >>> for i in total:
            >>>    for j in i:   
            >>>       try :
            >>>           i[i.index(j)] = float(re.sub(',', '', j))
            >>>       except:
            >>>           pass
            >>> print(i)        
    ```
  + 3-4. csv파일 데이터 분석
