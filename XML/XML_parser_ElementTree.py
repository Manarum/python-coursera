#Parse text and attribute from xml

import xml.etree.ElementTree as ET
data='''<stuff>
<users>
    <user x="3">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user x="2">
        <id>009</id>
        <name>Chen</name>
    </user>
</users>
</stuff>'''

tree=ET.fromstring(data)
ls=tree.findall('users/user')
print('User count:', len(ls))
for i in ls:
    print('ID:',i.find('id').text)
    print('Name:',i.find('name').text)
    print('Attribute:',i.get('x'))
