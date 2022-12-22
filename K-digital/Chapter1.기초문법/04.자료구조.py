#!/usr/bin/env python
# coding: utf-8

# # 4. 자료구조

# ### 1. 리스트 [ ]
# 순서를 가지는 객체의 집합

# In[7]:


subway = [ 10, 20, 30 ]
subway


# In[8]:


subway = ["유재석", "조세호", "박명수"]
subway


# In[9]:


# 조세호씨가 몇 번째 칸에 타고있는지?
subway.index('조세호')


# In[10]:


# 다음 정류장에서 하하 탑승
subway.append('하하')
subway


# In[12]:


# 정형돈씨를 유재석/조세호 사이에 태움
subway.insert(1, "정형돈")
subway


# In[13]:


# 마지막 칸에서 부터 하차
subway.pop()


# In[14]:


subway.pop()
subway


# In[15]:


subway.pop()


# In[16]:


subway


# In[20]:


# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
subway


# In[21]:


subway.count("유재석")


# In[23]:


# 정렬도 가능
num_list = [5,2,3,4,1]
num_list.sort()


# In[24]:


# 순서 뒤집기 가능
num_list.reverse()
num_list


# In[25]:


num_list.clear()
num_list


# In[26]:


# 다양한 자료형 함께 사용 가능
mix_list = ['조세호', 20, True]
mix_list


# In[27]:


num_list = [5,2,4,3,1]
num_list.extend(mix_list)
num_list


# ### 2. 사전 {key : value }

# In[30]:


cabinet = {3: "유재석", 100: "김태호"}
cabinet[3]


# In[31]:


cabinet[100]


# In[33]:


cabinet.get(3)


# In[40]:


cabinet.get(5, "사용가능")  # get()은 밸류 없어도 오류 x, 다음 명령 실행


# In[38]:


cabinet[5]  # [] 은 밸류 없으면 오류 발생.
print('hi') 


# In[41]:


print(3 in cabinet)


# In[42]:


print(5 in cabinet)


# In[44]:


# 새 손님
cabinet[3] = "김종국"
cabinet[4] = '조세호'
cabinet


# In[45]:


# 손님 퇴장
del cabinet[3]
cabinet


# In[46]:


# key들만 출력
cabinet.keys()


# In[47]:


# value들만 출력
cabinet.values()


# In[48]:


# key, value 동시 출력
cabinet.items()


# In[51]:


# 목욕탕 폐정
cabinet.clear()
cabinet


# ### 3. 튜플 ( )
# + 내용 변경/추가 불가
# + 리스트보다 처리 속도가 빠름

# In[53]:


menu = ("돈까스", "치즈까스")
menu[0]
menu[1]


# In[54]:


menu.add("생선까스")  # 오류발생!


# In[59]:


name = "김종국"
age = 20
hobby = "코딩"
(name, age, hobby)


# In[60]:


name, age, hobby = "유재석", 30, "체육"


# In[61]:


name


# ### 4. 세트(집합) { }
# + 중복 안됨, 순서 없음

# In[62]:


my_set = {1,2,3,3,3}
my_set


# In[63]:


java = {"유재석", "하하", "양세형"}
python = set(['유재석', '박명수'])


# In[64]:


# java와 python 모두 할 수 있는 개발자
java&python


# In[65]:


java.intersection(python)


# In[66]:


# java or python 할 수 있는 개발자
java|python


# In[67]:


java.union(python)


# In[68]:


# 차집합(java 할수있지만 python은 못하는 개발자)
java - python


# In[69]:


java.difference(python)


# In[70]:


# python 할 수 있는 사람이 늘어남
python.add("김태호")
python


# In[72]:


# java를 잊었어요
java.remove("양세형")
java


# ### 5. 자료구조의 변경

# In[74]:


menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))


# In[75]:


menu = list(menu)
type(menu)


# In[76]:


menu = tuple(menu)
type(menu)


# In[77]:


menu = set(menu)
type(menu)


# ### 6. 퀴즈
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다.
# 
# + 조건1: 댓글은 20명이 작성, 아이디는 1~20
# + 조건2: 댓글 내용과 무관하게 추첨하되 중복 불가
# + 조건3: random 모듈의 shuffle과 sample을 활용
# 
# + 출력예제
# + -- 당첨자 발표 --
# + 치킨 당첨자:
# + 커피 당첨자: [ , , ]
# + -- 축하합니다! --

# In[78]:


from random import *


# In[85]:


id = list(range(1,21))
id


# In[87]:


shuffle(id)
id


# In[92]:


winners = sample(id, 4)  # 4명 중에서 1명은 치킨, 3명은 커피


# In[93]:


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다! --")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




