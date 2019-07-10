# 1. Bithumb 페이지를 가지고 온다.
import requests
import bs4
import csv

response = requests.get('https://www.bithumb.com/') # 요청을 보내 응답을 받음 # url의 전체 가지고옴
html = response.text # 응답받은 객체에서 html 문서를 string으로 가지고 옴
    # 현재 html의 타입은? string(문자) -> 이는 html형태가 아니라 그냥 문자 -> 의미없음(메모장에 적는 느낌) -> class, id, tag로 접근할 수 있게 도와주는 것이 beuatifulsoup

# 2. BeautifulSoup 모듈을 이용하여 string type의 html을 파싱한다.(import는 상단에 한번에 적는다)
soup = bs4.BeautifulSoup(html, 'html.parser') #우리가 가지고온 html문서를 파싱한 결과 -> 우리가 가지고 올 수 있는 객체가 됨

# 3.각 코인의 정보가 담겨있는 table row 데이터를 list의 형태로 가져오기
    # 한 줄을 item으로 삼고 모든 테그를(tr을) 하나의 리스트로 가지고 올 것이다.(btc, eth, xrp 등..)
coins = soup.select('.coin_list tr') #coin_list 안에 있는 tr에 접근하겠다. 
    # 필요한 것들을 선택 #coins는 <tbody coin_list>밑에 있는 tr들(btc, eth 등을 가지고옴)
    # .coin_list tr: class가 가지고 있는 모든 하위tr 가지고옴
    # .coin_list > tr: 무조건 coin_list 바로 밑에 있는 tr을 가지고 와라

# 4. 각 코인을 순회하며 필요한 정보만 추출한다.
for coin in coins: # coin == tr
    coin_name = coin.select_one('td:nth-child(1) > p > a> strong').text # 단어만 빼내겠다.
    coin_name = coin_name.replace("NEW", '') # coin_name = coin.select_one('td:nth-child(1) > p > a> strong').text.replace("NEW", '') 해도 같은 결과
    coin_price = coin.select_one('td:nth-child(2) > strong').text
    print(coin_name, coin_price)
    # coin: 각각 하나의 tr, coins: tr 전체
    # 각 코인의 이름과 시세, 데이터를 추정
    # coin_name 때 활용 tableAsset > tbody > tr:nth-child(1) [여기까지 coin] > td:nth-child(1)
    # coin_princ 때 활용 tableAsset > tbody > tr:nth-child(1) > td:nth-child(2)

# 5. csv writer를 이용해 정보를 저장한다.
with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f) # csv_writer한테 파일 전체 넘겨주기

#6. 보낼 정보를 만든다
    for coin in coins: # coin == tr
        coin_name = coin.select_one('td:nth-child(1) > p > a> strong').text.replace("NEW", '').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text 
            # 가격이 천원 이상이면 ,가 생김 -> 따라서 ""로 감싸서 하나의 데이터로 만든다는 것 -> 1000원 미만의 것은 ""생기지 않음  # 원, ','지우면 조금 더 깔끔하게 나옴
        data = (coin_name, coin_price) # 튜플형식으로 만들어주기!!! 
        csv_writer.writerow(data) # but 이때, name 뒤에 공백 생김! -> 이를 지우기 위해서는 strip()필요
        print(data)
