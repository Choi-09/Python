#!/usr/bin/env python
# coding: utf-8

# # 14. 그룹화
# 동일한 값을 가진 데이터끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[2]:


df.groupby('학교')


# In[3]:


df.groupby('학교').get_group('북산고')


# In[4]:


df.groupby('학교').get_group('능남고')


# In[5]:


df.groupby('학교').mean()  # 계산가능한 데이터들의 평균값


# In[6]:


df.groupby('학교').median()  # 각 그룹의 중앙값


# In[7]:


df.groupby('학교').size()  # 각 그룹의 크기 정보


# In[9]:


df.groupby('학교').size()['능남고']   # 학교로 그룹화를 한 후 '능남고'에 해당하는 데이터의 수


# In[11]:


df.groupby('학교')['키'].mean()   # 학교로 그룹핑 한 후 '키' 데이터에 대해 평균값 추출


# In[13]:


df.groupby('학교')[['국어', '영어', '수학']].mean()   # 학교로 그룹핑 한 후 국어,영어,수학 데이터의 평균 추출


# In[15]:


df['학년'] = [3,3,2,1,1,3,2,2]  # 학년 컬럼 추가


# In[16]:


df


# In[18]:


df.groupby(['학교', '학년']).mean()   # 학교별, 학년별 평균 데이터


# In[20]:


df.groupby('학년').mean()  # 학년별 평균 데이터


# In[23]:


df.groupby('학년').mean().sort_values('키', ascending = False)   
# 학년 그룹핑 후 계산가능한 데이터의 평균값을 낸 후 '키' 순서대로 내림차순 정렬


# In[26]:


df.groupby(['학교','학년']).sum()


# In[29]:


df.groupby('학교')[['이름', 'SW특기']].count()  # 학교로 그룹화를 한 뒤에 학교별 SW특기 데이터의 수를 가져옴


# In[32]:


school = df.groupby('학교')
school['학년'].value_counts()   # 학교로 그룹화 한 후 학년별 인원수를 가져옴


# In[35]:


school['학년'].value_counts().loc['북산고']  #  학교로 그룹화 한 후(school변수) 북산고등학교에 대해 학년별 인원수를 가져옴


# In[36]:


school['학년'].value_counts().loc['능남고'] # 학교로 그룹화 한 후(school 변수) 능남고등학교에 대해 학년별 인원수를 가져옴


# In[38]:


school['학년'].value_counts(normalize = True).loc['북산고']   # 학생들의 수 데이터를 비율로 비교


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




