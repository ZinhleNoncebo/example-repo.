# Open user.txt and read each username and password
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(", ")
        users[username] = password
