#UTF-8 recommended
#print(ord("A"))
#urllib even more simple browser
import urllib.request,urllib.parse,urllib.error
import bs4, ssl
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #since we get back data in bites we need to decode data 
print('-'*15)
#fhand=urllib.request.urlopen('http://netacad.com/courses/cybersecurity/introduction-cybersecurity')
#for line in fhand:
#    print(line.decode().strip())


#Get all hyperlink from a current page
# Ignore SSL cert errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
html=urllib.request.urlopen(url, context=ctx).read() #returns entire web-page 
soup=bs4.BeautifulSoup(html,'html.parser') #getting back an object

tags=soup('a') #asking for anchor tag <a href=""></a>
for tag in tags:
    print(tag.get('href',None))