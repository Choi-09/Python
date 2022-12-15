#!/usr/bin/env python
# coding: utf-8

# # 2. 출생아 수 및 합계출산율

# ### 파일에서 필요한 데이터만 불러오기

# In[2]:


import pandas as pd
df = pd.read_excel('142801_20221215185755750_excel.xlsx', skiprows = 2, nrows = 2, index_col=0)
# nrows 는 헤더부분을 제외한 데이터.
df


# In[6]:


df.index.values  # '출생아 수' 행을 인식하지 못해서 자세히 보니 숨어있는 값이 있음


# ### 행 이름 바꾸기

# In[7]:


df.rename(index={'출생아\xa0수':'출생아 수', '합계\xa0출산율': '합계 출산율'},inplace = True)


# In[9]:


df.index.values


# In[10]:


df.loc['출생아 수']


# In[12]:


df.iloc[0]  # 0번째 행 출력


# ### row와 column 변환

# In[14]:


df = df.T  # row와 column 변환


# In[15]:


df


# ### 데이터 시각화

# In[17]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[20]:


plt.plot(df.index, df['출생아 수'])
plt.plot(df.index, df['합계 출산율'])
# 단위가 달라서 y축 차이가 많이 난다!. x축은 공유하되 y축 단위는 추가해서 따로 보여보자


# ### x축 공유, y축 나누기
# + ax1.twinx()

# In[24]:


fig, ax1 = plt.subplots(figsize =(10,7))
ax1.plot(df.index, df['출생아 수'],color = '#ff812d', marker = '^')

ax2 = ax1.twinx()  #x축을 공유하는 쌍둥이 axis
ax2.plot(df.index, df['합계 출산율'], color = '#ffd100', marker = 'o')


# ### y축 단위 설정
# + set_ylim()
# + set_yticks() <br/>
# 
# ### y축 레이블
# + set_ylabel()

# In[34]:


fig, ax1 = plt.subplots(figsize =(13,5))
ax1.set_ylabel('출생아 수(천 명)')
ax1.set_ylim(250, 700)  
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'],color = '#ff812d')


ax2 = ax1.twinx()  #x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율(가입여성 1명당, 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color = '#ffd100', marker = 'o')


# ### '출생아 수' 그래프에 수치 표시
# + for idx, val in enumerate()

# In[51]:


fig, ax1 = plt.subplots(figsize =(13,5))
ax1.set_ylabel('출생아 수(천 명)')
ax1.set_ylim(250, 700)  
ax1.set_yticks([300,400,500,600])
bar = ax1.bar(df.index, df['출생아 수'],color = '#ff812d')
for idx, val in enumerate(df['출생아 수']):  # enumerate(): 원소의 인덱스와 밸류에 함께 접근 
    ax1.text(idx, val + 10, val, ha='center')
    

ax2 = ax1.twinx()  #x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율(가입여성 1명당, 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color = '#ffd100', marker = 'o', ms = 12, lw = 3, mec = 'w', mew = 3)


# ### '합계 출산율' 그래프에 수치 표시

# In[57]:


fig, ax1 = plt.subplots(figsize =(13,5))
ax1.set_ylabel('출생아 수(천 명)')
ax1.set_ylim(250, 700)  
ax1.set_yticks([300,400,500,600])
bar = ax1.bar(df.index, df['출생아 수'],color = '#ff812d')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val + 10, val, ha='center')
    

ax2 = ax1.twinx()  #x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율(가입여성 1명당, 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color = '#ffd100', marker = 'o', ms = 12, lw = 4, mec = 'w', mew = 3)
for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val + 0.075, val, ha = 'center')


# ### 꺾은선 그래프 스타일 추가
# + marker, ms, lw, mec, mew

# In[59]:


fig, ax1 = plt.subplots(figsize =(13,5))
fig.suptitle('출생아 수 및 합계 출산율')
ax1.set_ylabel('출생아 수(천 명)')
ax1.set_ylim(250, 700)  
ax1.set_yticks([300,400,500,600])
bar = ax1.bar(df.index, df['출생아 수'],color = '#ff812d')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val + 10, val, ha='center')
    

ax2 = ax1.twinx()  #x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율(가입여성 1명당, 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color = '#ffd100', marker = 'o', ms = 12, lw = 4, mec = 'w', mew = 3)
for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val + 0.075, val, ha = 'center')

