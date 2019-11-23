with open("userinfo.txt","r",encoding='utf-8') as fp:
    data = fp.readlines()

users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)

print(users)