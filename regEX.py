import re
x="I remeber having a dream about the 7 number I saw a set of 7s either 777 or 77777 or even 7777777"
y=re.findall('[0-9]+',x) #findall method matches the regEx pattern and extracts that match, puts the match into a list
print(y)
test="I Andrey"
y_test=re.findall('[AEIOU]+',test) #[AEIOU]set of characters but like just a single character if it finds from the set one character it puts into a list
print(y_test)
email="From andrejk@gmail.com Sat Jan 5 09:12 test@SS.lt"
x_email=re.findall('^From \S+@\S+',email) #['From andrejk@gmail.com']
y_email=re.findall('\S+@\S+',email) #['andrejk@gmail.com', 'test@SS.lt']
z_email=re.findall('^From (\S+@\S+)',email) #['andrejk@gmail.com'] "()" parenthesis indicate where to start parse from but without "From" it's just more precise method to parse string
print(x_email)
print(y_email)
print(z_email)