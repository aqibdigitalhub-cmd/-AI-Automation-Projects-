client_names = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"]
for name in client_names:
    print(name)

    client_names = ["Ali", "Ahmed", "Sara"]

for name in client_names:
    print("Hello", name, "Welcome to our service!")


client_names = ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"]

number = 1

for name in client_names:
    print(number, name)
    number = number + 1


client_budget = 350

if client_budget >= 300:
    print("Qualified Lead")
else:
    print("Needs Review")


client_budget = 250

if client_budget >= 300:
    print("Qualified Lead")
else:
    print("Needs Review")

    def greet(name):
        print("Hello", name)
    greet("Aqib")


client_names = [
    "Ali",
    "Ahmed",
    "Sara",
    "Usman",
    "Ayesha",
    "Bilal",
    "Hassan",
    "Zara",
    "Hamza",
    "Fatima"
]

def greet(name):
    print("Hello", name, "- Welcome to our service!")

for client in client_names:
    greet(client)


clients = []

while True:
    print("\n--- Client Menu ---")
    print("1 = Add")
    print("2 = Remove")
    print("3 = Exit")

    choice = input("Apna option select karein: ")

    if choice == "1":
        name = input("Client ka naam likhein: ")
        clients.append(name)
        print(name, "add ho gaya.")

    elif choice == "2":
        name = input("Kis client ko remove karna hai? ")

        if name in clients:
            clients.remove(name)
            print(name, "remove ho gaya.")
        else:
            print("Yeh client list mein nahi hai.")

    elif choice == "3":
        print("Program band ho raha hai.")
        break

    else:
        print("Invalid option. 1, 2 ya 3 select karein.")