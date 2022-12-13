#!/usr/bin/env python
# coding: utf-8

# # 15. 산점도 그래프
# 데이터의 상관관계 표현 <br/>
# + plt.scatter()

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[2]:


import pandas as pd
df = pd.read_excel('../Pandas/score.xlsx')
df


# In[5]:


# 학생들의 영어,수학성적 분포 확인

#학년추가
df['학년'] = [3,3,2,1,1,3,2,2]
df


# In[6]:


plt.scatter(df['영어'], df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')


# ### 점 크기 랜덤으로 변경

# In[16]:


import numpy as np
sizes = np.random.rand(8) * 1000
sizes


# In[17]:


plt.scatter(df['영어'],df['수학'], s = sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')


# ### 학년별 점 색상 구분하기
# + sizes = df['열명']

# In[23]:


sizes = df['학년'] * 500  # 1학년 = 500, 2학년 = 1000, 3학년 = 1500
plt.scatter(df['영어'],df['수학'], s = sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')


# ### 점 색상 변경
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
# 
# + c = df['학년']
# + cmap = ' '

# In[26]:


plt.scatter(df['영어'],df['수학'], s = sizes, c = df['학년'], cmap='viridis', alpha = 0.6)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')


# ### colorbar
# + plt.colorbar()
# + ticks
# + label
# + shrink = (0~1사이)
# + orientation = 'horizontal'

# In[32]:


plt.figure(figsize = (10,10))
plt.scatter(df['영어'],df['수학'], s = sizes, c = df['학년'], cmap='viridis', alpha = 0.6)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks = [1,2,3], label = '학년', shrink = 0.5, orientation = 'horizontal')

