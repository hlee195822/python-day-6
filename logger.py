user_name =input("what is your name, vistor?")

with open ("guest_list .txt", "a") as file:
    file.write(Hank + "\n")