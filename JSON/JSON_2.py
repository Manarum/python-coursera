import json

data='''{
"name":"Chuck",
"phone":{"type":"intel",
        "number":"+1234"},
"email":{"hide":"yes"}
}'''

info=json.loads(data)
print('Nested Dictionary:',info)
print('Name:',info["name"])
print('Phone:',info["phone"]["number"])