# 열기모드
# r: 읽기, w: 쓰기(write - 오버라이트), a: 추가(append)
f = open('ssafy.txt', 'w') # 경로에 들어간 파일 열기
for i in range(10):
    f.write(f'this is line {i + 1} \n') # 작성을 하겠다 // \n: 그 다음줄로 내리겠다
f.close() # 어떤 내용을 작업하고 마친 후에 제대로 저장하지 않으면 날라갈 수 있음 -> close해줘야 날아가지 않음. 안정적

with open('with_ssafy.txt', 'w') as f:# 컨텍스트 매니저 -> 코드블럭 생성! -> if 문해서 엔터치면 코드블럭인 것 -> 그 안에서 작업할 수 있게 만들어줌. 그 블럭을 벗어나면 알아서 정리해줌. # 연 파일의 이름은 f이고, 블럭을 생성해야하므로 :가 필요! / 위와 같은 것!(f = ~)
    for i in range(10):
        f.write(f'this is line {i + 1}\n') 

with open('ssafy_txt', 'w', encoding='utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n']) # 몇줄 스트링을 넣을지 리스트받아 결정가능
