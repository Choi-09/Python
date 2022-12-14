#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 모듈, 인코딩
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# ### 1. 데이터 불러오기

# In[66]:


import pandas as pd
df = pd.read_csv("./03_암발생자수_.csv", encoding= 'cp949')
df


# ### 2. 열명 변경
# + names(df) <- c('암종별', '성별', '연령별', '발생자수', '조발생률')

# In[67]:


df.columns = ['암종별', '성별', '연령별', '발생자수', '조발생률']
df


# ### 3. 열 데이터 타입 확인
# + str(df)

# In[27]:


df.info()


# ### 4. 1행 삭제
# + df <- df[-1,] 

# In[68]:


# 행, 열 조회
df.loc[0, '암종별']
df.iloc[0,0]


# In[69]:


# 1행 삭제
df = df.iloc[1:,:]
df


# ### 5. 특정행 열 조회
# + df[1:3,c('암종별', '발생자수')] 

# In[29]:


df.loc[[1,3], ['암종별', '발생자수']]


# ### 6. 값 변경 ("-" > 0)
# + df$발생자수 <- ifelse(df$발생자수 == "-", 0, df$발생자수)<br/>
# <br/>
# + df$조발생률 <- ifelse(df$조발생률 == "-", 0, df$조발생률)<br/>

# ##### 6-1 값 변경(1)
# numpy의 np.where() 사용

# In[32]:


import numpy as np


# In[ ]:


# R의 ifelse는 파이썬의 np.where()
df['발생자수'] = np.where(df['발생자수'] == '-', 0, df['발생자수'])
df['발생자수']


# temp = list(df['발생자수])
# temp = [int(s.replace("-",'0')) for s in temp]
# df['발생자수] = temp


# In[ ]:


df['조발생률'] = np.where(df['조발생률'] == '-', 0, df['조발생률'])
df['조발생률']

# temp = list(df['조발생률'])
# temp = [float(s.replace("-",'0')) for s in temp]
# df['조발생률'] = temp


# In[ ]:


df.info()


# ##### 6-2 값 변경(2)
# 함수 정의

# In[71]:


# 반복되는 코드는 함수로 만들어 사용할 수 있다.
# temp 함수 만들기
def func(col, df):
    temp = list(df[col])
    temp = [float(s.replace("-",'0')) for s in temp]
    df[col] = temp


# In[ ]:


for c in ['발생자수', '조발생률']:
    func(c, df)


# In[ ]:


df.info()


# ### 7. 데이터 타입 변경
# + df$발생자수 <-  as.numeric(df$발생자수)<br/>
# <br/>
# + df$조발생률 <- as.numeric(df$조발생률)<br/>

# In[ ]:


# 타입 변경(1)
df['발생자수'] = df['발생자수'].astype('int')
df['발생자수']


# In[ ]:


# 타입 변경(2)
df['조발생률'] = pd.to_numeric(df['조발생률'])
df['조발생률']


# In[ ]:


# 암 코드 뒷자리 추출(리스트를 새로만드는데[] s가 lt안에서 반복, )
lt = list(df['암종별'].unique())
lt = [s[-3:-1] for s in lt]
lt


# In[ ]:


lt = [int(s) for s in lt]  # 문자형 숫자로 이루어진 원소를 숫자형으로 변환. 
lt


# ### 8. '모든암' 제거하고 연령별이 '계'인 데이터 추출
# + df2 <- df %>%
#   filter(암종별 != "모든 암(C00-C96)") %>% 
#   filter(연령별 == "계")
# 
# +  df21 <- df2 %>% 
#   filter(성별 == "계")
# 
# + df22 <- df2 %>%
#   filter(성별 != "계")

# In[101]:


df1 = df[(df['암종별']== "모든 암(C00-C96)") & (df['연령별'] != "계") & (df['성별']== "계")]
df1


# ### 9. 특정 열가져오기
# + df21 <- df21[, c('암종별', '발생자수')] <br/>
# 
# + df22 <- df22[, c('암종별', '성별', '발생자수')] <br/>

# In[ ]:


df11 = df[(df['암종별']== "모든 암(C00-C96)") & (df['연령별'] != "계") & (df['성별']== "계")]\
        [['연령별', '발생자수']]
df11


# In[ ]:


# 인덱스 설정하기
df11 = df11.set_index("연령별")
df11


# In[104]:


df11.plot()
plt.show()


# In[ ]:


df12 = df[(df['암종별']== "모든 암(C00-C96)") & (df['연령별'] != "계") & (df['성별']!= "계")]\
        [['연령별', '성별', '발생자수']]
df12


# ### 10. seaborn 으로 그래프 그리기
# 필요한 데이터 추출(탐색적데이터분석: EDA)

# In[118]:


df2 = df[(df['암종별'] != "모든 암(C00-C96)") & (df['연령별'] != "계") & (df['성별']!= "계")]


# In[121]:


g = df2.groupby(['암종별', '성별']).mean()[['발생자수', '조발생률']]


# In[120]:


import seaborn as sns
# seaborn: 자동으로 평균값 구해서 그래프 그린다.
sns.barplot('암종별', '발생자수', hue='성별', data = df2)
plt.xticks(rotation = 90)
plt.show()

# 까만 막대: 표준편차

