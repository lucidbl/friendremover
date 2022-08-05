import requests
import time

token = {"authorization":"MTAwMDUyODM1NzIwMjU5MTg2NQ.GVDSeZ.VK39aKcvqOV2i4Qm9ZaBQP3RO7TqOdSWdBJuW4"}

friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers = token)

for friend in friends.json():
    friendz = friend["id"]
    requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friendz}", headers = token)
    time.sleep(0.5)
