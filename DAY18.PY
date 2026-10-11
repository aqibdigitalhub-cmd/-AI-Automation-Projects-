
with open('clients.txt', 'w') as f:
    f.write('Ahmed, ahmed@email.com')

with open("clients.txt", "r") as f:
        print(f.read())


import csv

with open('clients.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email'])
    writer.writerow(['Ahmed', 'ahmed@email.com'])
    writer.writerow(['Sara', 'sara@email.com'])

with open('clients.csv', 'r', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)        


import csv

clients = [
    ['Ahmed', 'ahmed@email.com'],
    ['Sara', 'sara@email.com'],
    ['Ali', 'ali@email.com'],
    ['Ayesha', 'ayesha@email.com'],
    ['Usman', 'usman@email.com'],
    ['Fatima', 'fatima@email.com'],
    ['Bilal', 'bilal@email.com'],
    ['Zara', 'zara@email.com'],
    ['Hassan', 'hassan@email.com'],
    ['Hamza', 'hamza@email.com']
]

with open('clients_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email'])
    writer.writerows(clients)

with open('clients_data.csv', 'r', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

import csv

with open('clients_data.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)

    for client in reader:
        name = client['Name']
        email = client['Email']

        message = f"Hello {name}, welcome to our service!"

        print("To:", email)
        print("Message:", message)
        print("--------------------")      


import pandas as pd

df = pd.read_csv('clients_data.csv')

print(df.head())