
client = {
    'name': 'Ahmed',
    'email': 'ahmed@g.com',
    'budget': 500
}

print(client)
print(client['name'])
print(client['email'])
print(client['budget'])


clients = [
    {'name': 'Ahmed'},
    {'name': 'Sara'}
]

for client in clients:
    print(client['name'])


import json

# Python dictionary
client = {
    'name': 'Ahmed',
    'email': 'ahmed@g.com',
    'budget': 500
}

# Python dictionary ko JSON string mein convert karna
json_data = json.dumps(client)
print(json_data)

# JSON string ko Python dictionary mein convert karna
python_data = json.loads(json_data)
print(python_data['name'])
print(python_data['budget'])


import json

api_response = '''
{
    "status": "success",
    "client": {
        "name": "Ahmed",
        "email": "ahmed@g.com",
        "budget": 500
    }
}
'''

data = json.loads(api_response)

print(data["status"])
print(data["client"]["name"])
print(data["client"]["email"])
print(data["client"]["budget"])