import requests as req 
from bs4 import BeautifulSoup



# START: Target Site
web_raskakcija = 'https://www.raskakcija.lt'
web_raskakcija_robots = 'https://www.raskakcija.lt/sitemap.xml'

# rules:
"""
User-agent: *
Crawl-delay: 10
sitemap: https://www.raskakcija.lt/sitemap.xml
"""

web = req.get(web_raskakcija)

print(web)

