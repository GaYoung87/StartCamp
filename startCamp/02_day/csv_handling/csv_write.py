dinner = {
    '양자강': '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',} # 원래 딕셔너리는 for문 돌 수 없다.

# dinner.keys() -> 리스트 타입으로 [양자강, 김밥카페..]로 나옴
# dinner.values() -> 리스트 타입으로 [번호]로 나옴
# 이때, key, value 둘다 가지고 오려면 items로 하면 ok
# 1. 그냥만들기 (String formating)
with open('dinner.csv', 'w', encoding="utf-8") as f: #encoding : 한글이 들어갔으므로
    for item in dinner.items():  #dinner를 item, dictionary형태로 만들 수 있음
    # [['양자강', '02-557-4211'], ['김밥카페', '02-553-3181'], ...] -> 리스트로 만들어줌
        f.write(f'{item[0]},{item[1]}\n') # 양자강,02-557-4221(우리가 원하는 csv형식)


# 2. csv writer 사용
import csv
with open('dinner.csv', 'w', encoding='utf=8', newline='') as f: #newline옵션에 아무것도 두지 않겠다고 해야함. window는 기본적으로 한줄씩 띄어져서 나옴
    csv_writer = csv.writer(f) #f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item) #writerow라는 함수

# 함수의 매개변수를 넘길 때, 옵션을 줄 때는(encoding, newline) = 앞뒤로 한칸 씩 띄지말고 붙여서 작성해라! 그것이 컨벤션!
# 코딩 후 맨 마지막 한 줄 빈칸으로 두는 것이 컨벤션!