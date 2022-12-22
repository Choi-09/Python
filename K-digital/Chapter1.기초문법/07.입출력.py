#!/usr/bin/env python
# coding: utf-8

# # 7. 입출력

# ### 1. 표준입출력

# In[9]:


# sep = ''
print("Python", "Java", sep=',')


# In[10]:


# end = ''
print("Python", "Java", end ="?")
print("무엇이 더 재밌을까요?")


# In[13]:


import sys


# In[15]:


# file = sys.stdout / sys.stderr
print("Python", "Java", file=sys.stdout)
print("무엇이 더 재밌을까요?", file=sys.stderr)


# In[25]:


# .ljust(), .rjust()
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# In[29]:


# .zfill() 
for num in range(1,21):
    print("대기번호: ", str(num).zfill(3))


# In[31]:


answer = input("아무 값이나 입력하세요:")
print("입력하신 값은:", answer,"입니다.")


# ### 2. 다양한 출력포멧
# + 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

# In[39]:


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보 
print("{0: >10}".format(500)) 


# In[42]:


# 양수 일때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500)) 

print("{0: >10}".format(-500)) 


# In[43]:


# 왼쪽정렬, 빈칸을 _로 채우기 
print("{0:_<+10}".format(500))


# In[44]:


# 세자리 마다 콤마 찍기
print("{0:,}".format(10000000000))


# In[45]:


print("{0:+,}".format(10000000000))


# In[46]:


print("{0:+,}".format(-10000000000))


# In[47]:


# 3자리마다 콤마, 부호, 자릿수 확보


# In[49]:


# 돈이 많아면 행복하니까 빈자리는 ^로 채워주기 
print("{0:^<+30,}".format(1000000000))


# In[50]:


# 소수점 출력
print("{0:f}".format(5/3))


# In[52]:


# 소수점 특정 자리수까지만 표시(소수점 3째자리에서 반올림)
print("{0:.2f}".format(5/3))


# ### 3. 파일 입출력

# In[79]:


# 새로운 파일 생성 및 내용작성 
score_file=open("score.txt", 'w', encoding = 'utf-8')
print("수학:0", file=score_file)
print("영어:30", file= score_file)
score_file.close()


# In[80]:


# 기존 파일 뒷부분에 내용 append
score_file = open("score.txt", 'a', encoding = 'utf-8')
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()


# In[81]:


# 파일 전체 읽기 .read()
score_file = open("score.txt", 'r', encoding = 'utf-8')
print(score_file.read())
score_file.close()


# In[84]:


# 파일 내용 한 줄씩 불러오기 .readline()
score_file = open("score.txt", 'r', encoding ='utf-8')
print(score_file.readline(), end='') #줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이등
print(score_file.readline(), end='') 
print(score_file.readline(), end='') 
print(score_file.readline(), end='') 
score_file.close()


# In[85]:


# while문을 사용하여 파일 한 줄씩 불러오기 
score_file = open("score.txt", 'r', encoding ='utf-8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = '')
score_file.close()


# In[86]:


# list에 값을 넣어서 파일내용 불러오기 
score_file = open("score.txt", 'r', encoding ='utf-8')
lines = score_file.readlines()
for line in lines:
    print(line, end='')
    
score_file.close()


# ### 4. pickle
# + 용량이 많은 파일을 바이너리로 저장하고 읽기  

# In[87]:


import pickle


# In[91]:


profile_file = open("profile.pickle", 'wb')


# In[92]:


profile = {"이름":"박명수", "나이": 30, "취미":["축구", '야구',' 골프']}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장 
profile_file.close()


# In[96]:


profile_file = open("profile.pickle", 'rb')
profile = pickle.load(profile_file) # file에 있는 정보를 profile로 불러온다.
print(profile)
profile_file.close()


# ### 5. with
# + 파일을 자동 저장 후 닫는다. 

# In[98]:


import pickle


# In[100]:


with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


# In[102]:


with open("study.txt", 'w', encoding = 'utf8') as study_file:
    study_file.write("파이썬을 공부하고 있어요")


# In[103]:


with open("study.txt", "r", encoding = 'utf8') as study_file:
    print(study_file.read())


# ### 6. 퀴즈
# + 매주 1회 작성하는 보고서 
# + '- X 주차 주간보고 -
# + 부서 :
# + 이름 :
# + 업무 요약:
# 
# + 1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# + 조건: 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만든다.

# In[111]:


def report():
    cnt = 1
    while cnt <= 50:
        with open(f"{cnt}주차.txt", 'w', encoding = 'utf8') as report_file:
            report_file.write(f"- {cnt} 주차 주간보고 -")
            report_file.write("\n부서 :")
            report_file.write("\n이름 :")
            report_file.write("\n업무 요약:")
        cnt += 1
report()

