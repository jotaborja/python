import json

data = '''{
    
    "name" : "jota",
    "phone" : {
        "type" : "intl",
        "number" : "1234"
        },
    "email" : {
        "hide" : "yes"
        }
    }'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide', info["email"]["hide"])
