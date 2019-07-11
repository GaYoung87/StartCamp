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


if __name__ == '__main__':
    app.run(debug=True)