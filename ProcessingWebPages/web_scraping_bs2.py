from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
table_data = soup.find_all('td')
result = 0
for i in range(len(table_data)):
    result += int(table_data[i].text)

print(result)
