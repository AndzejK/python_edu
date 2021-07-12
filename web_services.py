import xml.etree.ElementTree as ET, json
data='''
<person>
    <name>Andrey</name>
    <phone type="intl">
        049091703*
    </phone>
    <email hide="yes"/>
</person>
'''

tree=ET.fromstring(data) #getting back an object
print('Name:',tree.find("name").text)
print('Attr:',tree.find('email').get('hide'))
print('-'*15)
data_in_jsn=''' 
{
    "name":"Andrey",
    "phone":{
        "type":"intl",
        "number":"049091703*"
    },
    "email":{
        "hide":"yes"
    }
}
'''
info=json.loads(data_in_jsn) #returns the dictionary
print(info)#print dictionary
print('-'*15)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
print('phone:',info["phone"]["number"])
print('-'*15)
input='''[
   {
        "id":"01",
        "x":"1",
        "name":"Andrey"
    },
    {
        "id":"02",
        "x":"2",
        "name":"Chuck"  
    }
]'''
info_v1=json.loads(input)
print(info_v1)
print('-'*15)
print(info_v1[0]["name"])
print('-'*15)
print('User count:',len(info_v1))
print('-'*15)
for x in info_v1:
    print('Name',x['name'])
    print('Id',x['id'])
    print('Attribute',x['x'])
    print('-'*15)

