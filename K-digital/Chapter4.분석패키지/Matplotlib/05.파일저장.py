#!/usr/bin/env python
# coding: utf-8

# # 5. 파일저장
# 그래프를 파일로 저장하기

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[2]:


x = [1,2,3]
y = [2,4,8]


# In[5]:


plt.plot(x,y)
plt.savefig('graph.png')


# In[6]:


plt.plot(x,y)
plt.savefig('graph1.png', dpi = 100)


# In[8]:


plt.figure(dpi = 200)   # plt.figure(dpi) 는 주피터 화면에 나오는거.
plt.plot(x,y)
plt.savefig('graph2.png', dpi = 100)  # plt.savefig(dpi) 는 저장 화면 

