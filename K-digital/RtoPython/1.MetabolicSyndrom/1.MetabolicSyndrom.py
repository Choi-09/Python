#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# import csv

# In[135]:


import pandas as pd
import csv


# ### 1. 파일불러오기

# In[253]:


df = pd.read_csv("../국민건강보험공단_건강검진정보_20211229.csv", encoding = 'cp949')


# In[137]:


df.head(5)


# ### 2. 열명 확인 및 변경

# In[254]:


df.columns


# + 필요한 열 가져오기

# In[255]:


dlist = list(df.columns)
dlist


# In[256]:


for i in dlist:
    print(i)


# + 리스트를 튜플로 만들기

# In[274]:


for i,c in enumerate(dlist):
    print(i, c)


# + 열 변경

# In[275]:


df2 = df[['성별코드', '허리둘레', '수축기 혈압', '이완기 혈압', '식전혈당(공복혈당)', '트리글리세라이드', 'HDL 콜레스테롤']]
df2.head(5)


# + 열 명 변경

# In[276]:


lt = list(df2.columns)
lt


# + list 안의 공백 한번에 제거하기

# In[277]:


lt = [c.replace(' ','') for c in lt]
lt


# In[278]:


lt[4] = '공복혈당'
lt


# In[279]:


df2.columns = lt
df2.head()


# ### 3. Nan 값 삭제하기

# In[280]:


df2.info()


# In[281]:


df2 = df2.dropna(axis = 0)
df2.info()


# ### 4. 데이터 가공(R to Python)

# In[282]:


import numpy as np


# (1) 높은 혈압(130/85mmHg 이상) <br/>
#     df검진정보$높은혈압 <- ifelse((df검진정보$수축기.혈압 >= 130) | (df검진정보$이완기.혈압 >=80), 1, 0)

# In[283]:


df2['높은혈압'] = np.where((df2['수축기혈압'] >= 130) | (df2['이완기혈압']>=85), 1, 0)
df2.head(5)


# (2) 높은 혈당(공복 혈당 100mg/dL 이상) <br/>
#     df검진정보$높은혈당 <- ifelse(df검진정보$식전혈당.공복혈당. >= 100,  1, 0)

# In[284]:


df2['높은혈당'] = np.where((df2['공복혈당'] >=100), 1,0)
df2.head(5)


# (3) 높은 중성지방(트리글리세라이드 150mg/dL 이상) <br/>
#     df검진정보$높은중성지방 <- ifelse(df검진정보$트리글리세라이드 >=150,  1, 0)
# 

# In[285]:


df2['높은중성지방'] = np.where(df2['트리글리세라이드']>150,1,0)
df2.head(5)


# (4) 낮은 HDL 콜레스테롤 수치(남성은 40mg/dL 미만, 여성은 50mg/dL 미만)<br/>
#     df검진정보$낮은HDL콜레스테롤 <- ((df검진정보$성별코드==1)&(df검진정보$HDL.콜레스테롤 <40)|(df검진정보$성별코드==2)&(df검진정보$HDL.콜레스테롤 <50))
# 

# In[286]:


df2['낮은 HDL콜레스테롤'] = np.where(((df2['성별코드']==1)&(df2['HDL콜레스테롤']<40)) | ((df2['성별코드']==2)&(df2['HDL콜레스테롤']<50)),1,0)
df2.head(5)


# (5) 복부 비만(남성 90cm 이상, 여성 85cm 이상)
# df검진정보$복부비만 <- ((df검진정보$성별코드==1)&(df검진정보$허리둘레 >=90)|(df검진정보$성별코드==2)&(df검진정보$허리둘레 >=85))

# In[287]:


df2['복부비만'] = np.where(((df2['성별코드']==1)&(df2['허리둘레']>=90)) | ((df2['성별코드']==2)&(df2['허리둘레']>=85)),1,0)
df2.head(5)


# ### 5. 데이터 판별

# (6) 합계 점수 내기 <br/>
# df대사증후군판별$점수 <- df대사증후군판별$혈압 + 
#                          df대사증후군판별$혈당 + 
#                          df대사증후군판별$중성지방 + 
#                          df대사증후군판별$콜레스테롤 + 
#                          df대사증후군판별$복부비만

# In[288]:


df2['점수 합계'] = df2['높은혈압'] + df2['높은혈당'] + df2['높은중성지방'] + df2['낮은 HDL콜레스테롤'] + df2['복부비만']
df2


# (7) 점수 구간별 위험군 나누기<br/>
# df대사증후군판별$결과 <- ifelse(df대사증후군판별$점수  < 1 , "정상", 
#                        ifelse(df대사증후군판별$점수 <= 2, "주의군", "위험군"))
# 

# In[289]:


df2['결과'] = np.where(df2['점수 합계'] < 1, "정상",
                np.where(df2['점수 합계']<=2, "주의군","위험군"))

df2


# (8) 성별코드코드로 남/녀 구분하기

# In[290]:


df2['성별'] = np.where(df2['성별코드'] ==1,"남자","여자")
df2


# (9) () table > goupby로 그룹짓기 <br/>
# table(df대사증후군판별$성별코드, df대사증후군판별$결과)

# In[292]:


df2.groupby(['성별','결과']).count()['성별코드']


