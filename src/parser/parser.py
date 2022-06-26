import re

LISTS = {
    "bot" : "https://raw.githubusercontent.com/d3fc0n6/BotList/master/list", # Needs to be converted to 64 IDs
    "cheater" : "https://raw.githubusercontent.com/d3fc0n6/CheaterList/main/CheaterFriend/64ids",
    "tacobot" : "https://raw.githubusercontent.com/d3fc0n6/TacobotList/master/64ids",
    "pazer" : "https://raw.githubusercontent.com/d3fc0n6/PazerList/master/list.cfg" # Needs to be converted to 64 IDs and cleaned up
}

ID64_MAGIC_NUMBER = 76561197960265728

PAZER_REGEX = re.compile(r"\d+")

def to_64(id: int) -> int:
    return id + ID64_MAGIC_NUMBER

def parse_bot_list(list: str) -> str:
    list = list.splitlines()
    ids = []
    for i in list:
        ids.append(to_64(int(i)))
    return ids

def parse_pazer_list(list: str) -> str:
    list = list.splitlines()
    ids = []
    for i in list:
        ids.append(to_64(int(PAZER_REGEX.search(i).group(0))))
    return ids

