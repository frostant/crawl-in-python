import requests
import sys
import webbrowser

param = {"wd":"Python"}
r = requests.get('http://www.baidu.com/s',params=param)

print(r.url)
webbrowser.open(r.url)

# 下文的两个post指令无法正常运行
data = {'firstname':'frost','lastname':'ant'}
rr = requests.post('http://pythonscraping.com/files/processing.php',data=data)
print(rr.text)

file = {'uploadFile':open('C:/Users/sky48/Desktop/樱花庄.jpg','rb')}
r1 = requests.post('http://pythonscraping.com/files/processing2.php',file=file)
print(r.text)

