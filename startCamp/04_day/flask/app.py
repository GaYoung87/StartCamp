from flask import Flask,render_template, request #request는 사용자의 요청을 핸들링할 수 있음(flask내에 존재) #flask앱은 하나의 서버!
import requests
app = Flask(__name__)


@app.route('/') # 사용자가 이 경로로 들어왔을 때 페이지를 보여준다 # / : 사용자가 들어올 수 있는 endpoint -> 루트
def index():
    return 'Hello World!' # local host => 127.0.0.1 -> 서버테스트를 위해.


@app.route('/greeting/<string:name>') #string이라고 명시해도 괜찮다!
def greeting(name):
    return render_template('greeting.html', html_name=name) # greeting.html은 app.py와 동일 경로여야한다. -> app.py가 flask밑에 있으니까 templates안에 greeting.html을 만든다.


@app.route('/ping')
def ping():
    return render_template('ping.html') #저장시켜 돌리면 /ping이라고 하면 나이 치면 주소가 /pong?age=24 이런 식으로 뜬다(요청 : /pong?age=24)


@app.route('/pong')
def pong():
    age = request.args.get('age') # 사용자가 보낸 입력값에서 꺼내겠다
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


# 실습 : ASCII art 흐름 알기!!!!!!!
@app.route('/ascii_input') # 사용자가 특정문자(Hello World)입력할 수 있는 페이지를 만들겠다
def ascii_input():
    return render_template('ascii_input.html') #input값 입력해라


@app.route('/ascii_result') # 다시 요청을 보내는 페이지
def ascii_result():
    text = request.args.get('text') # 입력값 받아야함 #input의 name을 text로 보냈기 때문에 text라고 한다.  # 사용자가 보낸 input값을 request함수를 통해 받는다
    # Ascii Art API를 활용해서 사용자의 input값을 변경한다.
    # ex. Message라는 단어를 ascii값으로 변경해줘 # 주소창에 치면 요청을 보내는 것 #요청보내는 것 = requests함수를 통해 url에 붙여 보냄
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    # print(response) 하면 console창에 response[200]이라고 뜸
    result = response.text # print(response.text)이렇게 하면 console창에 text뜬다
    return render_template('ascii_result.html', result=result)


# 로또!
# 회차, 번호 받아서 비교(실제 당첨번호와 비교해서 몇위인지 알려줌) 대부분의 route는 2개면 된다.
#1.사용자가 input(정보)을 입력할수있는 페이지 2.사용자가 그 페이지를 통해 우리에게 제출했을때 우리가 받아 계산하고 비교해서 사용자에게 다시 보내줄 수 있는 페이지

@app.route('/lotto_input') # 사용자가 입력할 수 있는 페이지만 전달
def lotto_input():
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result(): # 이름이 겹친다면 바꾸는게 낫다.
#사용자 입력값 받기
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split() # 리스트로 분해해야 확인하기 쉬워진다 -> list로 만들어야함 -> .split() #['1', '2', ,,,]->string형태

# 로또 실제 당첨번호 확인
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # 아까는 text라고 함. .json은 함수이기때문에 .json()으로 작성

    # Json타입의 파일을 python dictionary로 parsing해줘
    # 지금 사용자가 입력한 번호랑, 회차별 번호 다 가지고있음

    # 이제부터는 비교!
    # 내가한 것
    # winner = []
    # if str(lotto_info['drwtNo1']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo1'])
    # if str(lotto_info['drwtNo2']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo2'])
    # if str(lotto_info['drwtNo3']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo3'])
    # if str(lotto_info['drwtNo4']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo4'])
    # if str(lotto_info['drwtNo5']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo5'])
    # if str(lotto_info['drwtNo6']) in lotto_numbers:
    #     winner.append(lotto_info['drwtNo6'])
    # if str(lotto_info['bnusNo']) in lotto_numbers:
    #     winner.append(lotto_info['bnusNo'])
    # print(winner)

    # 선생님이 알려주신 방법
    winner = [] # [1, 2, ..] -> 숫자형태
    for i in range(1, 7): #1 ~ 6
        winner.append(str(lotto_info[f'drwtNo{i}']))

    print(lotto_numbers) # 사용자 도전번호
    print(winner)# 실제 당첨번호
    
# 번호 교집합 개수 찾기 
############## 사용자가 주는 input은 믿지 말아라 ##############  -> input확인작업 필요
    if len(lotto_numbers) == 6:             # 사용자 숫자가 딱 6개가 맞는지 확인
        matched = 0
        for number in lotto_numbers:        # 사용자 숫자를 하나씩 확인하면서 
            if number in winner:            # 당첨번호에 있는지 체크해서
                matched += 1                # 당첨시 matched를 1씩 증가시킨다.

        if matched == 6:
            result = '1등입니다!'
        elif matched == 5:
            if str(lotto_info['bnusNo']) in lotto_numbers:
                result = '2등입니다!'
            else:
                result = '3등입니다!'
        elif matched == 4:
            result = '4등입니다.'
        elif matched == 3:
            result = '5등입니다'
        else:
            result = '꽝입니다'
    else:
        result = '입력하신 숫자가 6개가 아닙니다.'

    return render_template('lotto_result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
    