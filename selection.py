import roles
import playerList
import random
from colorama import Fore

MaxApoc = random.randint(0, 4)
MaxCoven = random.randint(2, 4)


print("Formatting: ")
print("file.txt:")
print("Ethan")
print("Ben")
print("Etc")
print(" ")
path = input("Please paste the path to the file that has all the players: ").rstrip()


with open(path, 'r') as file:
    for line in file:
        playerList.playerList.append(line.strip())

MaxNeutral = len(playerList.playerList) - MaxApoc - MaxCoven - random.randint(5, len(playerList.playerList)-MaxCoven-MaxApoc+5)


def StartNewGame():
    Coven = roles.Coven()
    CovenCount = 0

    Apoc = roles.Apoc()
    ApocCount = 0

    Neutral = roles.Neutral()
    NeutralCount = 0

    Town = roles.Town()

    while playerList.playerList:

        playerfr = playerList.playerList[random.randint(0, len(playerList.playerList)-1)]

        if CovenCount < MaxCoven:
            Coven.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            CovenCount = CovenCount + 1

        elif ApocCount < MaxApoc:
            Apoc.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            ApocCount = ApocCount + 1

        elif NeutralCount < MaxNeutral:
            Neutral.select_role(playerfr)
            playerList.playerList.remove(playerfr)
            NeutralCount = NeutralCount + 1

        else:
            Town.select_role(playerfr)
            playerList.playerList.remove(playerfr)


StartNewGame()

for k, v in playerList.playerRoleList.items():

    color = Fore.WHITE

    if v in playerList.coven:
        color = Fore.RED
    if v in playerList.apoc:
        color = Fore.MAGENTA
    if v in playerList.neutral:
        color = Fore.YELLOW
    if v in playerList.town:
        color = Fore.GREEN

    print(color + f"{k}: {v}")