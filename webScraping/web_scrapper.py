import requests as req 
from bs4 import BeautifulSoup


web = req.get("https://www.livinn.lt")

web_url_no_item = req.get("https://www.livinn.lt/p/keltu-juros-druska-celtic-sea-salt-1-kg-cupp7153-lt")

web_url_w_item = req.get("https://www.livinn.lt/p/keltu-juros-druska-celtic-sea-salt-rupi-454-g-celt0008-lt")
web_url_string=web_url_w_item.text

# 1. HTML text (a string) is converted into a tree/ Beautiful Soup OBJECT with the help a parser such as 'lxml'
soup = BeautifulSoup(web_url_string,'lxml')

# 2. Now I can use Beautiful Soup's methods to work on this PARSE TREE/DOM
find_div=soup.find_all("div", class_="cart__control-container")
print(find_div)

# <div cart__control-block active error

# print(web_url.text)