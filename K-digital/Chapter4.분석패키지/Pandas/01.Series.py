#!/usr/bin/env python
# coding: utf-8

# # Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# - 데이터는 보통 행,열로 이루어져있는데 이것을 쉽게 처리.
# - 파이썬에서 데이터분석을 한다고 하면 대부분 판다스 사용

# + 주피터 노트북 단축키
# 
#     (b: 아래에 입력줄 추가) <br/>
#     (m: 마크다운으로 바꾸기) <br/>
#     (ctrl + ent: 실행) <br/>
#     (alt + ent: 실행하고 아래 입력줄 바로 추가) <br/>

# In[1]:


import pandas as pd  #판다스 임포트


# # 1. Series
# 1차원 데이터(정수, 실수, 문자열 등)

# ## Series 객체 생성
# 예) 1월 ~ 4월까지 평균 온도 데이터(-20,-10,10,20)

# In[4]:


temp = pd.Series([-20, -10, 10, 20])
print(temp)


# In[5]:


temp[0] #1월 온도


# In[7]:


temp[2] # 3월 온도


# # Series 객체 생성(Index 지정)

# In[12]:


temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr']) 
                                    # 인덱스를 지정하면 이름이 정해진다. 이후에 인덱스 이름으로 접근가능
temp


# In[14]:


temp['Jan'] # indext Jan에 해당하는 데이터 출력


# In[16]:


temp['Feb'] # indext Feb에 해당하는 데이터 출력


# In[19]:


# temp['Jun'] # 존재하지 않는 index 데이터는 오류발생


# In[ ]:




