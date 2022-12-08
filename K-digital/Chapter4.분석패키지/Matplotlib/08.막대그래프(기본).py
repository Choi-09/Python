#!/usr/bin/env python
# coding: utf-8

# # 8. 막대 그래프(기본)

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# In[8]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키


# ### bar 차트 그리기

# In[6]:


plt.bar(labels, values, color = 'purple')


# ### bar 컬러, 투명도 조절

# In[21]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키
colors = ['r', 'g', 'b']

plt.bar(labels, values, color = colors, alpha = 0.5)


# ### y축 데이터 범위 조절

# In[14]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키

plt.bar(labels, values)
plt.ylim(175,195)


# ### 그래프 두께 설정

# In[16]:


plt.bar(labels, values, width = 0.3)
plt.ylim(175,195)


# ### 글자끼리 겹칠때

# In[17]:


plt.bar(labels, values, width = 0.3)
plt.xticks(rotation=45)  # x축의 이름 값을 45도 기울임
plt.yticks(rotation = 45)  # y축의 이름 값을 45도 기울임


# ### X틱 이름만 바꿀 때

# In[20]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키
ticks = ['1번', '2번', '3번']

plt.bar(labels, values)
plt.xticks(labels, ticks, rotation = 90)

