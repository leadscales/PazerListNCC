import re
import requests

def steam64(id):
    return 76561197960265728 + int(id)

ids = str(requests.get("https://raw.githubusercontent.com/d3fc0n6/PazerList/master/list.cfg").content)

s = re.findall(r'\d+',ids)

with open("Pazer.txt","w") as f:
    for i in range(len(s)):
            f.write(str(steam64(s[i]))+" - ?\n")

print("Done, file saved to \"Pazer.txt\". Nullcore will automatically replace the question marks with actual player names once you encounter them in-game.")