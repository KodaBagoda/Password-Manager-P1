master_pwd = input("What is the master password: ")

def view():
    with open("password_manager.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            


def add():
    name = input("Enter the name of the entry: ")
    pwd = input("Enter the password for the entry: ")

    with open("password_manager.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new entry or retrieve an existing entry (view, add), press q to quit?: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue 