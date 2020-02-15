from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://stepik.org/media/attachments/lesson/209723/5.html'
resp = urlopen(url)
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
table_data = soup.find_all('td')
result = 0
for i in range(len(table_data)):
    result += int(table_data[i].text)

print(result)
