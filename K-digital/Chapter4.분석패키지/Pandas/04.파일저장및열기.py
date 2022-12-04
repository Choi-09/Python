#!/usr/bin/env python
# coding: utf-8

# # 4. 파일 저장 및 열기
# DataFrame 객체를 excel, csv, txt 등 형태의 파일로 저장 및 열기

# In[7]:


import pandas as pd


# In[8]:


data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
df = pd.DataFrame(data, index = ['1번', '2번', '3번',' 4번',' 5번', '6번', '7번',' 8번'])
df.index.name ='지원번호'
df


# ***
# ## 파일 저장하기
# ### CSV파일로 저장

# In[9]:


df.to_csv('score.csv', encoding = 'utf-8-sig')  # c드라이브 > 사용자 > user > PythonWorkPlace > Pandas


# In[10]:


df.to_csv('score1.csv', encoding = 'utf-8-sig', index = False) 


# ### text파일로 저장

# In[12]:


df.to_csv('score.txt', sep = '\t')  #tab으로 구분된 텍스트 파일


# ### excel 파일로 저장

# In[44]:


df.to_excel('score.xlsx')


# ***
# ## 파일 열기

# ## csv파일 열기

# In[17]:


df = pd.read_csv('score1.csv')
df


# In[19]:


df = pd. read_csv('score1.csv', skiprows = 1) # 지정된 갯수 만큼의 row를 건너뛴다
df


# In[21]:


df = pd.read_csv('score1.csv', skiprows = [1,3,5]) # 1,3,5 번째 row를 제외
df


# In[23]:


df = pd.read_csv('score1.csv', nrows = 4) #지정된 갯수 만큼의 row만 가져옴. nrows는 타이틀을 건드리지 않음.
df


# In[25]:


df = pd.read_csv('score1.csv', skiprows=2, nrows = 4) # 처음 2개 row는 무시하고 그 뒤 4개 row를 가져옴
df


# ### text파일 열기

# In[28]:


df = pd.read_csv('score.txt', sep = '\t')
df


# In[29]:


df = pd.read_csv('score.txt', sep = '\t', index_col = '지원번호')
df


# In[33]:


df = pd.read_csv('score.txt', sep = '\t')
df.set_index('지원번호', inplace = True)
df


# ## excel 파일 열기

# In[45]:


df = pd.read_excel('score.xlsx')
df


# In[48]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[61]:


df = pd.read_excel('score.xlsx', index_col = '지원번호')
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




