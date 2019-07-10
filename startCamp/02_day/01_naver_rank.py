# 요청보내는 url은 'https://www.naver.com'
# 우리가 원하는 것은 실검 -> 요소검사

import requests
import bs4
url = 'https://www.naver.com/'

selector = '.ah_k' #class selector이다 (이렇게 생긴 것을 추출하겠다)
# seletor로 가지고와서 하면 ok
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser') #parsing 위의 것에 접근할 수 있도록!
ranks = soup.select(selector)
print(ranks)

#<span class="ah_k">와 </span>은 필요 없다. -> 티르티르와 같은 text만 뽑고 싶다. -> for문으로 item 확인

for rank in ranks:
    print(rank.text) # 각 줄로 나옴