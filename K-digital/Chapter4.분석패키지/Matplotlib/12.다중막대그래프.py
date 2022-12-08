#!/usr/bin/env python
# coding: utf-8

# # 12. 다중 막대 그래프
# 여러 데이터를 나란히 보여준다.

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[3]:


df = pd.read_excel('../Pandas/score.xlsx',)
df


# + bar의 축 이동은 numpy의 개념으로 이해하자:)

# In[4]:


import numpy as np


# In[8]:


arr = np.arange(5)
arr


# In[9]:


arr + 100


# In[11]:


arr*3


# ### 한 그래프에 여러 데이터의 막대 그래프 그리기

# In[14]:


df.shape  #(row, column) 갯수


# In[17]:


N=df.shape[0]
N


# In[20]:


index = np.arange(N)
index


# In[23]:


w = 0.25
plt.bar(index - w, df['국어'])  # w: 막대 그래프의 x축 이동 
plt.bar(index, df['영어'])
plt.bar(index+w, df['수학']) 


# ### 그래프의 막대 굵기 조절로 겹치는 부분 없애기

# In[24]:


w = 0.25
plt.bar(index - w, df['국어'], width = w)  # w: 막대 그래프의 x축 이동 
plt.bar(index, df['영어'], width = w)
plt.bar(index+w, df['수학'], width = w) 


# ### 레이블(범례) 설정

# In[28]:


w = 0.25
plt.bar(index - w, df['국어'], width = w, label = '국어')  # w: 막대 그래프의 x축 이동 
plt.bar(index, df['영어'], width = w, label = '영어')
plt.bar(index+w, df['수학'], width = w, label ='수학')
plt.legend(ncol= 3)


# ### X축의 이름을 바꿔주기

# In[40]:


plt.figure(figsize = (10,5))
plt.title('학생별 성적')
w = 0.25
plt.bar(index - w, df['국어'], width = w, label = '국어')  # w: 막대 그래프의 x축 이동 
plt.bar(index, df['영어'], width = w, label = '영어')
plt.bar(index+w, df['수학'], width = w, label ='수학')
plt.legend(ncol= 3, loc = 'upper center')

plt.xticks(index, df['이름'], rotation=45)
plt.show()

