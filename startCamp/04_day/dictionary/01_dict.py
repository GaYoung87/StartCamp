# 1. dictionary 만들기
lunch1 = {
    '중국집': '02'
}
print(lunch1)

lunch2 = dict(중국집='02') #{'중국집': '02'}로 나옴
print(lunch2)


# 2. dictionary 내용 추가하기
lunch1['중국집'] # 02라고 나옴
lunch1['분식집'] = '031' # 이렇게 작성하면 내용 추가


# 3. ditionary 내용 가지고오기
idol = {
    'bts': {
        '지민': 24,
        'RM': 25
    }
}
#랩몬스터의 나이는?
print(idol['bts']['RM'])

print('==========================================')


# 4. dictionary 반복문 활용하기
# 기본 활용
for key in lunch1:
    print(key, lunch1[key])

# value만 가져오기
for value in lunch1.values():
    print(value)

# key만 가져오기
for key in lunch1.keys():
    print(key)

# .items() -> key, value 가져오기
for key, value in lunch1.items():
    print(lunch1.items())
    print(key, value)
