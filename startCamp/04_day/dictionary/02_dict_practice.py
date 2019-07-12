# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# 내 답
sum = 0
for value in score.values():
    sum += value
print(sum/len(score))


# 선생님 답 1.
total_score = 0
for subject_score in score.values():
    total_score += subject_score

average_score = total_score / len(score.values())
print(average_score)

# 선생님 답 2. 에러
# total_score = sum(score.values())

# print(total_score / len(score))







# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

# 내 답(노답 못품)
# for subject_score in scores.values():
#     for value in subject_score.values():

# 선생님 답 1.
# 1.a와 b의 딕셔너리에 접근한다.   2.
total_score = 0
count = 0 # 몇번의 점수를 더했는지

for person_score in scores.values():
    # print(person_score.values()) # dict
    total_score += sum(person_score.values()) # a의 토탈 값을 더하고, b의 토탈 값을 더한다.
    count += len(person_score)

average_score = total_score / count
print(average_score)










# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 선생님 답
for key, value in city.items():
    average_temp = sum(value) / len(value)
    print(f'{key} : {average_temp:.1f}') # f'' -> f strings  # 소숫점 관련 구글링



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# 선생님 답
# 각각 순환하면서 지역마다 값 3개를 돌고, 가장 온도가 낮았던 value 찾고, 지역추출 => 전체 12개의 모든 value를 비교하면서 가장 온도가 낮거나 높은 정보를 저장하고있다가 마지막에 나오는 친구들을 추출하는 방식




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')






print('===================')
# sum([1, 3, 4]) # 8
# len([1, 3, 4]) # 3
# max([1, 3, 4]) # 4
# min([1, 3, 4]) # 1