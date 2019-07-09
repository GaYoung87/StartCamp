# ssafy_txt파일을 읽어서 역순으로 reversed_ssafy.txt 파일로 저장

with open('ssafy_txt', 'r') as f:
    lines = f.readlines() # 왜 readlines로 읽냐면  list의 형식으로 각 라인을 item삼아서 반환한다.(각 라인을 item으로, list의 형태로 반환) # 뒤집는 작업을 리스트로 하면 편함.
    # print(lines)

# list 뒤집는 방법
lines.reverse() # 해당 리스트 뒤집기

with open('reversed_ssafy.txt', 'w') as f:
    for  line in lines:
        f.write(line)
