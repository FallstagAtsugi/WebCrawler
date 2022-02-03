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


bs = BeautifulSoup(response.text, 'html.parser')
# スクレイピングで特定の値を表示
bs_ul = bs.find('ul')

for bs_li in bs_ul.find_all('li'):
    bs_text = bs_li.text
    print(bs_text)

# CSSセレクタを使用して値を表示
div_curriculums = bs.select('div.curriculum_banner')
for div_curriculum in div_curriculums:
    a_tag = div_curriculum.find('a')

    curriculum_name = a_tag['title']
    href = a_tag['href']
    print('カリキュラム: {}, URL: {}'.format(curriculum_name, href))


# 集計結果を表示
url = "https://www.sejuku.net/blog/recommends"
search_word = 'python'
count = 0
response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')


articles = bs.select('article.vce-lay-b-child')

for article in articles:
    a_tag = article.find('a')
    article_title = a_tag['title']

    if search_word in article_title.lower():
        count += 1
        href = a_tag['href']
        print('タイトル: {}, nURL: {}'.format(article_title, href))

print('#'*50)
print('検索ワード: {}, 該当記事: {}個'.format(search_word, count))
print('#'*50)
