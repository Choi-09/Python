#!/usr/bin/env python
# coding: utf-8

# # 13. 함수 적용

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[2]:


df['학교'] = df['학교'] + '등학교'


# In[3]:


df


# ## appy  : 데이터에 함수 적용

# In[7]:


def add_cm(height):
    return str(height)+ 'cm'    # '키' 값을 int에서 str으로 바꾼 후 str타입의 'cm'를 붙인 값을 리턴한다.

df['키'] = df['키'].apply(add_cm)  # 키 데이터에 add_cm 함수를 호출한 결과 데이터를 반영
df


# In[9]:


def capitalize(lang):
    if pd.notnull(lang):    # NaN이 아닌지 확인
        return lang.capitalize()  # 첫글자는 대문자로, 나머지는 소문자로 바꿔준다. 여기서 capitalize는 내장함수.
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize)
df


# In[13]:


df['SW특기'].str.capitalize()  # 위와 같은 결과.


# In[22]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')


# In[23]:


df['SW특기'] = df['SW특기'].str.capitalize()  # 위와 같은 결과.
df

