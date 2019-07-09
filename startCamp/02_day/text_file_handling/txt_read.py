f = open('ssafy_txt', 'r')
all_text = f.read() # all text 전체를 불러온다(개행문자 포함!)
print(all_text)
f.close()


with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)


with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines() # 파일전체를 읽은다음에 라인을 리스트로 읽어옴 / lines에 this is line1~10까지 있음
    for line in lines:
        print(line.strip()) # line도 하나의 string type / strip : 개행문자 제거!(한줄씩 프린트하면 자동으로 개행문자를 띄게되는데 이미 prnit자체에 개행문자 있음)
