# 1. split함수를 사용
with open('dinner.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(',')) # 개행이 print에도 붙어서 엔터 두번넣은 것처럼 된다. ->.strip()으로 지워준다
                        # split안의 , 기준으로 문자열을 split한다.(list형태로)


# 2. csv reader 사용
import csv 
with open('dinner.csv', 'r', encoding='utf-8') as f: #utf-8 : 한글, 중국어, 이모티콘을 해석하기 위함
    items = csv.reader(f)
    for item in items:
        print(item)

