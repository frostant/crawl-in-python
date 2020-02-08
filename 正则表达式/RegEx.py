import re

pattern1 = "cat"
string = "the cat drink milk"
str1 = "the cat drank drank milk"
print(re.search(pattern1,string)) 

ptn = r"dr[ai]nk"  # r"dr[A-Z0-9]"
print(re.search(ptn,string))
print(re.search(ptn,str1))

match = re.search(r"(?P<id>\d+)","num:1571065")
print(match)

matchs = re.findall(r"r[au]n","run ren ran rnn")
matches = re.findall(r"ran|run","run ren ran rnn")
print(matchs)
print(matches)

replace = re.sub(r"ran","run","to ran or to run")
print(replace)

divide = re.split(r"[:;,\.]","a,b.c.dd:fa:s")
print(divide)

compile_re = re.compile(r"r[ua]n")
get_re = compile_re.search("a running dog")
print(get_re)

