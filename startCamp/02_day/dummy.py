# 주석 단축키 : ctrl + /
# Create dummy files
# touch라고 하면 파일 생성 -> 성과 이름을 랜덤으로 돌려서 500개의 랜덤한 파일을 만든다.
import os
import random

family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(500):
    cmd = f"touch {i+1}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)
