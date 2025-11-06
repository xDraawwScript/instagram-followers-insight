import json

followers_file="followers_1.json"
following_file="following.json"

with open(followers_file, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open(following_file, "r", encoding="utf-8") as f:
    following_data = json.load(f)

followers=set()
for entry in followers_data:
    value=entry["string_list_data"][0]["value"]
    followers.add(value)

following=set() 
for entry in following_data["relationships_following"]:
    title=entry["title"]
    following.add(title)

not_following_back=[]
for username in following:
    if username not in followers:
        not_following_back.append(username)

not_following_back.sort()

print(f"Tu suis {len(following)} comptes")
print(f"Tu as {len(followers)} abonnés")
print(f"{len(not_following_back)} ne te suivent pas en retour :\n")

for user in not_following_back:
    print("-", user)

with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for user in not_following_back:
        f.write(user + "\n")

print("\nEnregistré dans not_following_back.txt")