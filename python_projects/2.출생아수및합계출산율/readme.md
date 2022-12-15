## 2012년 ~ 2021년 출생아 수 및 합계 출산율 변화 추이
### 1. 나라지표 사이트에서 출생아 수 및 합계출산율 데이터 가져오기
  + import pandas
  + pd.read_excel('파일명', skiprows, nrows, index_col)

### 2. 행 이름 바꾸기
  + df.index.values : 최초 변경시 '해당 열이 없다'는 오류 발생 → 데이터에 숨은 값이 있어서 찾아냄
  + df.loc['행이름']  == df.iloc[행인덱스번호]  : [인덱스] 대괄호 안에 인덱스가 1개 있으면 행으로 인식. 

### 3. row와 column 변환
  + df.T : .T메소드로 row와 column 전치

### 4. 데이터 시각화
  + import matplotlib
  + subplot(): ax1, ax2 변수에 각 데이터를 넣고 한 그래프안에 모두 표시
  + ax1.twinx() : ax1과 x축을 공유하는 ax2그래프
  + set_ylim(시작값, 끝값) : y축이 표시되는 범위
  + set_yticks([v1, v2, v3]) : 표시되는 y축의 틱 단위
  + set_ylabel('레이블명') : 레이블명 설정
  + for idx, val in enumerated(): 튜플형태만 그래프에 붙일 수 있어서 index와 value가 튜플형태로 나오는 enumerated()함수 사용
  + marker, markerSize(ms), lineWidth(lw), markerEdgeColor(mec), marderEdgeWidth(mew) 설정
  
### 5. 결론
  + 2021년 기준 가임기 여성 1인당 0.8명의 자녀를 출산한다.

### 6. 질문(22.12.15)
  + 출산율이 감소하는 이유는?
  + 현재 시행중인 출산장려 정책은? 
  + 실직적으로 도움이 될 만한 정부 지원방안은?

### 7. 참고사이트
  + 지표누리: http://index.go.kr/common/error.html
