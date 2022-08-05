import requests
import time

token = {"authorization":"token"}

friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers = token)

for friend in friends.json():
    friendz = friend["id"]
    requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friendz}", headers = token)
    time.sleep(0.5)
