#!/usr/bin/env python
# coding: utf-8

# # 9. 막대 그래프(심화)

# In[1]:


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = 'Apple Gothic'  # Mac용 
matplotlib.rcParams['font.size'] = 15  # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False


# ### 가로 bar 그래프
# h만 붙이면 된다!

# In[2]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키
plt.barh(labels, values, color = 'purple')


# ### x축 데이터 범위 수정

# In[4]:


labels = ['강백호', '서태웅', '정대만']  # 선수 이름
values = [190,187,184]  # 키
plt.barh(labels, values, color = 'purple')
plt.xlim(175,195)


# ### 그래프 안 패턴 넣기
# https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html

# In[8]:


bar = plt.bar(labels, values)
bar[0].set_hatch('//')  # /////
bar[1].set_hatch('xx')  # xxxxx
bar[2].set_hatch('..')  # .....


# ### 그래프 안 텍스트 넣기

# In[17]:


bar = plt.bar(labels,values)
plt.ylim(175,195)

for idx, rect in enumerate(bar):  #rect: 그래프 네모 안의 값을 가져옴
    plt.text(idx, rect.get_height()+0.5, values[idx], ha = 'center', color = "red")

