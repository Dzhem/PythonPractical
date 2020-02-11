from urllib.request import urlopen

html = urlopen('https://ru.wikipedia.org/wiki/Python'). \
    read().decode('utf-8')
str_html = str(html)
ans = []
state = 0
for c in str_html:
    if c == '<':
        state = 1
    elif c == '>':
        state = 0
    if state == 0:
        ans.append(c)
text_page = ''.join(ans)

print(text_page.count('C++'))
