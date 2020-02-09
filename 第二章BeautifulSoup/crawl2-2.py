from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/list.html"
).read().decode("utf-8")

# soup = BeautifulSoup(html,features='lxml')

soup = BeautifulSoup(html, features='lxml')

month = soup.find_all('li',{'class':'month'})
jan = soup.find_all('ul',{'class':'jan'})

for m in month:
    print(m.get_text())
for j in jan:
    print(j.get_text())

# 可以把beautifulsoup和正则表达式结合有更强大的功能

