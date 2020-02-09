from bs4 import BeautifulSoup
from urllib.request import urlopen
import re,sys
import random

base_url = "https://baike.baidu.com"
start = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):
    url = base_url + start[-1]

    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, features='lxml')
    print(i,soup.find('h1').get_text()," url: ",start[-1])

    sub_urls = soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        start.append(random.sample(sub_urls,1)[0]["href"])
    else :
        start.pop()
        
sys.exit()

# 下方为脑补的爬虫代码

base_url = "https://baike.baidu.com"
start = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

url = base_url + start[-1]

html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, features='lxml')

# print(html)
cont = soup.find('h1').get_text() + "url: " + start[-1]
print(cont)

web_url = soup.find_all('a',{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

for web in web_url:
    # print(web['href'])
    htmls = urlopen(base_url+web['href']).read().decode("utf-8")
    step = BeautifulSoup(htmls,features='lxml')
    ned = step.find('h1').get_text()
    print(ned)

