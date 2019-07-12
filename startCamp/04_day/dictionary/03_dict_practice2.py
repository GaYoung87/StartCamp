ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'harry',
            'manager': '노구하',
            'class president': '박나율',
            'groups': {
                'A': ['이길현', '우동균', '이승현', '이가경', '이병재'],
                'B': ['차진권', '박성진', '심규현', '남승현'],
                'C': ['신승호', '조현호', '이병주', '박홍은'],
                'D': ['조규홍', '조수지', '임소희', '이해인'],
                'E': ['박상원', '고병권', '김준호', '신정우', '박나율']
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'pro-gj'
        }
    }
}


"""
난이도* 1. 지역(location)은 몇 개 있나요?
출력예시)
4
"""
print('==========Q1==========')
print(len(ssafy['location']))




"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
print('=========Q2==========')
# 풀이 1
flag = False # 먼저 입력을 해줘야한다! 아니면 무한으로 돈다
for library in ssafy['language']['python']['python standard library']:
    if library == 'requests':
        flag = True

print(flag)

# 풀이 2
for library in ssafy['language']['python']['python standard library']:
    if library == 'requests':
        flag = True
    else:
        flag = False
print(flag)

# 풀이 3
print( 'requests' in ssafy['language']['python']['python standard library'])




"""
난이도** 3. dj 반의 반장의 이름을 출력하세요.
출력예시)
박나율
"""
print('=========Q3==========')
print(ssafy['classes']['dj']['class president'])




"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""
print('=========Q4==========')
for key in ssafy['language'].keys():
    print(key)




"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
pro-gj
"""
print('=========Q5==========')
for name in ssafy['classes']['gj'].values():
    print(name)




"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
print('=========Q6==========')
for key, value in ssafy['language']['python']['frameworks'].items():
    print(f'{key}는 {value}이다.')
# 꼭 key, value라고 하지 않고 name, attr(속성)이라고 작성해도 됨 // 이때 .values(), .keys(), .items()는 변함없음




"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 김준호
"""
print('=========Q7==========')
import random
dangbun = random.choice(ssafy['classes']['dj']['groups']['E']) # random.choice : 한명 선택
print(f'오늘의 당번은 {dangbun}')
# E그룹의 [0]은 박상원 => print(f"오늘의 당번은 {ssafy['classes']['dj']['groups']['E'][0]}") 할때 f''가 아닌 f""여야 하는 이유는 'classes'등이 있으므로 ""가 되어야한다.