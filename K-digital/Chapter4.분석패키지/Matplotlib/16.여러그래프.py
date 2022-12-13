#!/usr/bin/env python
# coding: utf-8

# # 16. 여러 그래프
# 여러 그래프 한꺼번에 보여주기

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


# ### fig, axs = plt.subplots( 행, 열)

# In[5]:


fig, axs = plt.subplots(2,2, figsize = (15,10))  # 2x2에 해당하는 plot들을 생성
fig.suptitle('여러 그래프 넣기')


# ### 그래프 그리기
# + axs[행,열]
# + set_title()
# + set(xlabel = , ylabel = )
# + set_facecolor()

# In[14]:


fig, axs = plt.subplots(2,2, figsize = (15,10))  # 2x2에 해당하는 plot들을 생성
fig.suptitle('여러 그래프 넣기')

# 첫 번째 그래프
axs[0,0].bar(df['이름'], df['국어'], label = '국어점수')  # 데이터 설정
axs[0,0].set_title('첫 번째 그래프')  # 제목
axs[0,0].legend()  # 범례
axs[0,0].set(xlabel = '이름', ylabel = '점수') # x,y축 label
axs[0,0].set_facecolor('lightyellow')  # 전경색
axs[0,0].grid(linestyle = '--', linewidth = 0.5)  # 격자 스타일

# 두 번째 그래프
axs[0,1].plot(df['이름'], df['수학'], label = '수학')
axs[0,1].plot(df['이름'], df['영어'], label = '영어')

# 세 번째 그래프
axs[1,0].barh(df['이름'], df['키'])

# 네 번재 그래프
axs[1,1].plot(df['이름'], df['사회'], color = 'g', alpha = 0.5)

