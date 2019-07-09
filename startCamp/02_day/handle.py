#더미의 결과에 500개의 모든 파일에 앞에 SAMSUNG이라는 단어를 추가할 것!
# 저장해야 돌아간다!!!!! 아 제발!! 저장하는데 익숙해지자..
import os # 우리의 window라는 컴퓨터가 os를 할 수 있게 시키는 것 

os.chdir(r'C:\Users\student\TIL\startCamp\02_day') # 500개의 지원서가 있는 곳으로 이동함 / chdir = change directory(r'주소')
# 파일 이름이 있어야 바꾸던지 한다.
# 현재는 500개 지원서가 있는 곳에 있음

filenames = os.listdir('.') # 특정 경로로부터 모두 가지고온다. / 현재 디렉토리에 있는 모든 파일 이름들을 가지고 온다.
# 이 때 dummy.py같은 것들은 바꾸면 안됨.

for filename in filenames:
    # 확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
    
    if extension == '.txt':
        # os.rename(filename, f'SSAFY_{filename}') # 첫번째 인자로 넘어간 이름을, 두번째 인자로 넘어간 이름으로 바꾼다.
        os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))
        # string할 때 '' 앞에 f를 쓰면 ok
    # SAMSUNG -> SSAFY라면 다른것 다 동일하고 os.rename(filename(문자열), filename.replace("SAMSUNG_", "SSAFY_"))
#import os : 컴퓨터가 할 수 있는 일들을 하는 아이 (이름바꾸기, directory바꾸기)
#os.chdir(r'폴더주소')
#os.listdir(".")
#os.rename(filename)