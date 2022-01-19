import re

WhatsappChat = open('_chat.txt', 'r')
lines = WhatsappChat.readlines()

users = {}
print("Since", lines[0][0:23])

for line in lines[1:]:
    message = str(line.strip())
    result = re.search('] (.*): ', message)
    if result:
        user = result.group(1)
        if ":" not in user:
            if users.get(user) is not None:
                users[user] = users[user] + 1
            else:
                users[user] = 1

sorted = sorted(users.items(), key=lambda x: x[1])
for user, count in sorted:
    print(user, ": ", count)
