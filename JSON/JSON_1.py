import json

data='''[
{"name":"Chuck",
"id":"1",
"phone":"+233456"},
{"name":"Chen",
"id":"5",
"phone":"+567789"}]
'''

info=json.loads(data)
print('Nested List:',info)
print('User count:',len(info))
for i in info:
    print('Name:',i["name"])
    print('ID:',i["id"])
    print('Phone:',i["phone"])