#!/usr/bin/env python
# coding: utf-8

# # 10. DataFrame 활용

# In[3]:


import pandas as pd


# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[18]:


df = pd.read_excel('../Pandas/score.xlsx',)
df


# ### 꺾은선(plot) 그래프 그리기

# In[6]:


plt.plot(df['지원번호'], df['키'], marker = 'o')


# ### 여러 데이터로 꺾은선 그래프 그리기
# + 그리드 그리기

# In[ ]:


plt.plot(df['지원번호'],df['영어'], label = '영어')
plt.plot(df['지원번호'],df['수학'], label = '수학')
plt.legend()
plt.grid()


# In[17]:


plt.plot(df['지원번호'],df['영어'], label = '영어')
plt.plot(df['지원번호'],df['수학'], label = '수학')
plt.grid(axis = 'x', color = 'purple', alpha = 0.5, ls = "--")

