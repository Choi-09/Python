#!/usr/bin/env python
# coding: utf-8

# # 12. 데이터 수정

# In[1]:


import pandas as pd
df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# ## Column 수정

# In[6]:


df['학교'].replace({'북산고' : '상북고', "능남고" : "무슨고"}, inplace = True)  # replace 를 딕셔너리 형태로 정의해준다.
df


# In[7]:


df["SW특기"].str.lower()


# In[11]:


df['SW특기'] = df["SW특기"].str.upper()
df


# In[16]:


df['학교'] = df['학교'] + '등학교'
df


# ## Column 추가

# In[20]:


df['총합'] = df['국어'] + df['영어']+df['수학']+df['과학']+df['사회']
df


# In[22]:


df['결과'] = 'Fail'  # 결과 컬럼을 추가하고 전체 데이터는 Fail로 초기화
df


# In[25]:


df.loc[df['총합'] > 400, '결과'] = 'Pass'  # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트
df


# ## Column 삭제

# In[27]:


df.drop(columns = ['총합'])  # 총합 컬럼 삭제


# In[29]:


df.drop(columns = ['국어', '영어', '수학'])  # 국어, 영어, 수학 컬럼 삭제


# ## Row 삭제

# In[32]:


df.drop(index = '4번')


# In[36]:


filt = df['수학'] < 80  # 수학이 80미만인 학생 필트
df[filt]


# In[37]:


df[filt].index


# In[39]:


df.drop(index = df[filt].index)  # 수학이 50점 미만인 학생 row 데이터 삭제


# ## Row 추가

# In[41]:


df.loc['9번'] = ['이정환', '해남고등학교', 184,90,90,90,90,90,'Kotlin', 450, "Pass"]
df


# ## Cell 수정

# In[43]:


df.loc['4번', 'SW특기'] = 'Python'  # 4번학생의 SW특기를 Python으로 수정
df


# In[45]:


df.loc['5번', ['SW특기', '학교']] = ['C', '능남고등학교']
df


# In[46]:


df


# ## Column 순서 변경

# In[50]:


cols = list(df.columns)
cols


# In[52]:


df = df[[cols[-1]] + cols[0:-1]]  # 맨뒤에 있는 결과 Column을 앞으로 가져오고, 나머지 Column들과 합쳐서 순서 변경
df


# ## Column의 이름 변경

# In[56]:


df.columns = ['Result', 'Name', 'School', 'Height', 'Korean', 'English', 'Math', 'Science', 'Social', 'SW Lan', 'Sum']
df

