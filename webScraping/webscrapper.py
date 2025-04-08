import requests as req 
from bs4 import BeautifulSoup


web = req.get("https://www.livinn.lt")
web_url_no_item = req.get("https://www.livinn.lt/p/keltu-juros-druska-celtic-sea-salt-1-kg-cupp7153-lt")
web_url_w_item = req.get("https://www.livinn.lt/p/keltu-juros-druska-celtic-sea-salt-rupi-454-g-celt0008-lt")
web_url_string=web_url_w_item.text

soup = BeautifulSoup(web_url_string,'lxml')

# <div class="cart__control-container"
find_div=soup.find_all("div", class_="cart__control-container")
print(find_div)

# <div cart__control-block active error

# print(web_url.text)