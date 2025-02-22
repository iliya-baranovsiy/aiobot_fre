import json

with open("config.json", mode="r", encoding="utf-8") as cnfg:
    data = json.loads(cnfg.read())

TOKEN = data.get("bot_token")