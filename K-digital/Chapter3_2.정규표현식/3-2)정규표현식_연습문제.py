import re

# 3-2장. 정규표현식으로 문자열 다루기 : 연습문제

# 1. 명령어 채우기
words = ['apple', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'above']
for i in words:
    m = re.match(r'a\D+', i)
    if m:
        print(i)
        

# 2. 정규식 채우기
a = '제 이메일 주소는 greatking@naver.com입니다. 오늘 저는 travel@daum.net 이라는 주소로 메일을 보내려고 합니다. 저는 apple@gmail.com. life@abc.co.kr 이라는 메일도 사용하고 있습니다.'
b = re.findall(r'[a-z]+@[a-z.]', a)     
print(b)
   

# 3.exam에서 연도만 추출해 리스트로 반환
exam = '저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2022년입니다.'
res = re.findall('\d+년', exam)
print(res)


# 4. 문장을 하나씩 추출하여 하나의 리스트에 저장할 때 필요한 명령어, 패턴
d = 'I have a dog. I am not a girl. You are not alone. I am happy.'
res = re.split(r'\.', d)
print(res)


# 5. 인물만 추출해 리스트에 저장. (중복값은 제거)
e = "Chandler: All right Joey, be nice. So does he have a hump? A hump and a hairpiece? Phoebe: Wait, does he eat chalk? Phoebe: Just, because, I don't want her to go through what I wnt through with Carl- oh!"
m = re.findall(r"[A-Za-z]+:", e)
#print(m)
P = list(set(m))
print(P)