from urllib.request import urlopen
from collections import Counter

html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html'). \
    read().decode('utf-8')
str_html = str(html)
ans = []
start_tag_code = 0
end_tag_code = 0
i = 0
while i < len(str_html):
    if str_html.find('<code>', end_tag_code) > -1:
        start_tag_code = str_html.find('<code>', end_tag_code)
        end_tag_code = str_html.find('</code>', start_tag_code)
        text_code = str_html[start_tag_code + 6: end_tag_code]
        ans.append(text_code)
        i = end_tag_code
    else:
        i = len(str_html)

count = Counter(ans)
max_v = 0
for k, v in count.items():
    if v > max_v:
        max_v = v

result = []
for k, v in count.items():
    if v == max_v:
        result.append(k)

print(' '.join(result))
