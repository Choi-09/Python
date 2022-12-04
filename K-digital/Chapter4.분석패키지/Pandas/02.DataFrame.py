#!/usr/bin/env python
# coding: utf-8

# # 2. DataFram
# 2차원 데이터(Series들의 모음)

# ## Data 준비
# 사전(dict) 자료구조를 통해 생성
# 예) 슬램덩크 주요 인물 8명에 대한 데이터

# In[1]:


data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
data


# In[6]:


data['이름']


# In[9]:


data['키']


# ## DataFrame 객체 생성

# In[10]:


import pandas as pd
df = pd.DataFrame(data)


# In[11]:


df


# ## 데이터 접근

# In[12]:


df['SW특기']


# In[14]:


df['키']


# In[16]:


df[['이름', '키']] # 두 개 이상의 컬럼을 한 번에 불러올 때는 대괄호 두번 써준다.


# ## DataFrame 객체 생성 (Index 지정)

# In[19]:


df = pd.DataFrame(data, index = ['1번', '2번', '3번',' 4번',' 5번', '6번', '7번',' 8번'])
df                      # index 갯수와 같이 적어줘야한다.


# ## DataFrame 객체 생성 (Column 지정)
# 데이터 중에서 원하는 컬럼만 선택하거나, 순서 변경 가능

# In[23]:


df = pd.DataFrame(data, columns = ['이름', '키', '학교'])
df

