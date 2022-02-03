import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
ua.chrome


# 取得するURL
url_top = "https://www.sejuku.net/blog/"
url_python = "https://www.sejuku.net/blog/curriculums-python"

# 侍エンジニアブログ トップページ取得
response = requests.get(url_top)
response.encoding = response.apparent_encoding

# スリープ
time.sleep(1)

# 侍エンジニアブログ Pythonページ取得
response2 = requests.get(url_python)
response2.encoding = response.apparent_encoding


print("--- 侍エンジニアブログ トップページ ---")
print(response.text)


print("--- 侍エンジニアブログ Pythonページ ---")
print(response2.text)


response_html = response.text

# 例えばresult.htmlに保存するなら…
with open('result.html', 'w', encoding='utf-8') as f:
    f.write(response_html)

print('ファイルに保存')


url = "https://www.sejuku.net/"


bs = BeautifulSoup(response.text, 'html.parser')
bs_ul = bs.find('ul')

for bs_li in bs_ul.find_all('li'):
    bs_text = bs_li.text
    print(bs_text)
