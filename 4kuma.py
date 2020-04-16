import requests
import re
import time
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

N = 274
url = 'https://www.google.co.jp/search'
html_data = []
ua = UserAgent()
header = {'user-agent':ua.chrome}

# session = requests.Session()

# retries = Retry(total=10,  # リトライ回数
#                 backoff_factor=1,  # sleep時間
#                 status_forcelist=[429]) 

# session.mount("https://", HTTPAdapter(max_retries=retries))

for i in range(N):
	k = i + 1
	number = str(k)
	episode = '第'+number.zfill(3)+'話'
	param =	'site:pachikuri.jp/4kuma ' + episode
	req = requests.get(url,params={'q':param},headers=header)
	# req = session.get(url=url,
    #                    headers=header,
    #                    params=param,
    #                    stream=True,
    #                    timeout=(10.0, 30.0))
	fpage_text = req.text
	#match = re.search(r'話(.+?)更新',fpage_text)
	match = re.search(r'https://pachikuri.jp/4kuma/(.+?)" ping=',fpage_text)
	try:
		match = "https://pachikuri.jp/4kuma/" + match.group(1)
	except AttributeError as e:
		match = "nourl"
	match_status_code = str(requests.get(match).status_code)
	with open('4kuma_url.txt', 'a') as f:
  		print(number+","  + match +", "+match_status_code, file=f)
	# print(number+" end")
	print(number+","  + match +", "+match_status_code)
	# print(number + match)
	time.sleep(60)

#print(html_data[207])

# for i in range(1):
# 	k = i + 1 
# 	number = str(k)
# 	param =	'site:pachikuri.jp/4kuma 第'+number.zfill(3)+'話'
# 	param =	'リラックマ'
# 	resp = requests.get(url,params={'q':param})
# 	resp.raise_for_status()
# 	# 取得したHTMLをパースする
# 	soup = bs4.BeautifulSoup(resp.text, "html.parser")
# 	# 検索結果のタイトルとリンクを取得
# 	link_elem01 = soup.select('.r > a')
# 	# 検索結果の説明部分を取得
# 	link_elem02 = soup.select('.s > .st')
# 	if(len(link_elem02) <= len(link_elem01)):
# 	    leng = len(link_elem02)
# 	else:
# 	    leng = len(link_elem01)    
# 	print(link_elem01)
# 	print(link_elem02)