from bs4 import BeautifulSoup

import requests

url = "https://www.pythonforbeginners.com/code-snippets-source-code/python-code-examples:"

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data)
print(soup)

#for link in soup.find_all('a'):
 #   print(link.get("herf))
