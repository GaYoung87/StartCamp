from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route('/') # @가 붙어있어서 데코레이터 -> 하는 일: www.google.com/search(search: end point라고 한다. -> /를 루트라고 이야기하고있다. 루트페이지를 들어갔을 때 Hello SSAFY라는 단어를 보여주는 것) -> 특정 endpoint에 왔을 때 함수를 작동시켜 결과를 보여줌
def hello(): # hello라는 함수를 만든 것 -> 그 함수의 반환값은 "Hello SSAFY!"
    # return 'Hello Jason!'
    return render_template('index.html') #index.html을 사람들한테 보여주겠다. -> templates 폴더 필수적으로 있어야하고, app.py와 같은 경로에 있어야하며, index.html이 있어야함.
    # 어떤 html 파일을 사람들에게 보여줄지 


@app.route('/ssafy') # /로 시작해야함
def ssafy():
    return 'Hello SSAFY!' # 링크 누르면 Hello Jason! 뜨고 거기에 /ssafy붙여주면 Hello SSAFY!로 바뀐다. 


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 8, 7)
    td = b_day - today
    return f'{td.days} 일 남았습니다!'


@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'


@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
        '''


# 함수와 함수 사이는 공란 두줄, ()안에 기호는 붙여서, 아니면 앞뒤로 한칸씩 띄고, ,뒤에는 한칸씩 띄기
# Variable Routing
# 연예인 이름만 달라지고, 반복하게하기!!
@app.route('/greeting/<name>') # IU
def greeting(name):  # name == IU
    return render_template('greeting.html', html_name=name) # greeting.html을 만들어서 보여주겠다**** 이는 templates라는 폴더에서 찾음. (name을 greeting.html안에서 html_name으로 쓸 수 있도록 옵션을 넣어줌)
# 파이썬에서 변수 넘기면 html 가서 변환시켜 주는 것이 진저(flask관련)
# html_name과 같은 변수는 해당 변수에서 html에서 사용가능

# string type이 아닌 다른 type으로 가능!
@app.route('/cube/<int:num>')
def cube(num):
    # return f'{num}의 3 제곱은 {num ** 3} 입니다.'
    result = num ** 3
    return render_template('cube.html', num=num, result=result)


# 실습 - 메뉴 주문서 넣기 사람 수만큼 메뉴 뽑아내는 것
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '김밥', '쫄면', '국밥', '짬뽕']
    order = random.sample(menu, people) # list -> type맞춰서 넣어줘야 error안남
    return str(order) # string 값으로 바꾸기 (return str(order) 가능! return f'메뉴는 {order}입니다.' 가능!)


@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '엔드게임', '알라딘', '너의결혼식'] # 사용자가 들어왔을 때 movies에 담아놓은 영화 목록 보여주기
    return render_template('movie.html', movies=movies) # 여러개가 있다면 -> movies


if __name__ == '__main__': 
    # 파이썬 파일들은 모두 모듈이다. 따라서 1. import hello -> print(hello.message) 가능! 그러면 @@@@@@hi@@@@@@@ 나옴   2. app.py에서 호출해서 실행하면 main 이아니라 hello가 나옴 // 직접 호출했을 때만 서버로서 활용하고, 아니면 우리는 선언된 다른 친구들에 접근할 때만(모듈에 접근할때만) app.py는 파이썬으로 직접 호출할때만 운영하겠다.
    # 파이썬으로 실행했을 때 name이라는 변수에는 main이라느 친구가 담긴다(name은 모든 파이썬에 있다). 모듈로써 실행하면 main이 아니지만, name이라고 지정해서 호출하면 main이 나온다.
    app.run(debug=True)
