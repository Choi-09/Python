# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:48:39 2022

@author: user
"""
#모듈 임포트
import re,os  

# python  파일이저장된 폴더에 friends101.txt파일 저장
# friends101.txt 파일 reading모드로 열기
# f = open('friends101.txt', 'r' )

# read한 txt파일을 변수에 저장
# s101 = f.read()

# s101(friends101.txt 내용 확인)
# print(s101)

'''
#모니카 라인 찾기
Monica_Line = re.findall(r'Monica:.+', s101)

# print(Monica_Line)   : Monica_Line을 리스트로 출력
for item in Monica_Line:    
    print(item,"\n")


# 빈 문자열을 저장하면 문자열 형식의 객체가 생성된다. 여기 Monica 텍스트를 문자열형식으로 저장한다.
monica = ''

# List 원소를 monica문자열에 추가
for i in Monica_Line:
    monica += i + "\n"
    
# Monica.txt라는 write 파일 생성
f = open('Monica.txt', 'w')

# 
f.write(monica)

f.close()
'''

'''
# 등장인물 찾기
char = re.findall("[A-Z][a-z]{1,7}:", s101)

ch = []
for c in list(set(char)):       # set(리스트명) : 저장된 값이 집합으로 바뀌면서 중복없이 출력
    ch.append((re.sub(r':', '', c)))    
    # .append() = 변수 += [ ]
    # 문자열 슬라이싱: 변수[인덱스]
print(ch)
'''

'''
# 등장인물 찾기: 모든 명령어를 한줄로 입력하기
char = [x[:-1]for x in list(set(re.findall(r'[A-Z][a-z]+: ', s101)))]

print(char)
'''

'''
# 괄호안의 문자열만 검색
paren_char = re.findall(r"\(.+?\)", s101)
print(paren_char)
'''

'''
# would가 포함된 문자열
os.chdir(r"C:\Python")
f = open('friends101.txt', 'r')
s101 = f.readlines()
f.seek(0)

'''
'''
for line in s101:
    if re.match(r"[A-Z][a-z]+:", line) and re.search('would', line):
        print(line)
'''
'''
would = [line for line in s101 if re.match(r"[A-Z][a-z]+:", line) and re.search('would', line)] 
# print(would)

# would_lines라는 스트링 객체 생성
would_lines = ''

#would의 인자를 would_lines에 넣기
for i in would:
    would_lines += i + "\n"
    
print(would_lines)

# would.txt라는 이름으로 새로운 파일 쓰기
newf = open('would.txt', 'w')

# would 리스트에 들어있는 원소 넣기
newf.writelines(would_lines)

# 파일을 닫으며 저장
newf.close()
'''


