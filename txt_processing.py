#UTF-8 recommended
#print(ord("A"))
#urllib even more simple browser
import urllib.request,urllib.parse,urllib.error
import bs4
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #since we get back data in bites we need to decode data 
print('-'*15)
#fhand=urllib.request.urlopen('http://netacad.com/courses/cybersecurity/introduction-cybersecurity')
#for line in fhand:
#    print(line.decode().strip())

url = input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=bs4.BeautifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))