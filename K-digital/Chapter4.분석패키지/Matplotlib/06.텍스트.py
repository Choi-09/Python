#!/usr/bin/env python
# coding: utf-8

# # 6. 텍스트

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


# In[3]:


plt.plot(x,y)


# In[12]:


plt.plot(x,y, marker ='o')

t = ['1', '2', '3']

for idx, txt in enumerate(t):
    plt.text(x[idx],y[idx] + 0.2, txt, ha='center', color = 'b')  #x좌표와 y좌표에 txt 넣어주고 # x좌표(수평정렬) 가운데정렬
    
    # enumerate() : 인덱스와 값에 접근 
    # enumerate(t) : t데이터의 값을 찍어준다.
    # 마커와 겹치지 않게 +0.2
    # ha: horizental align 
    # plt.text : 그래프 마커에 text넣어준다

