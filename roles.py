import random
import playerList

class Coven:
    def __init__(self):
        self.power_selected = False
        self.killing_selected = False
        self.power = ["Coven Leader", "Hex Master", "Witch"]
        self.killing = ["Conjurer", "Jinx", "Ritualist"]
        self.everythingelse = ["Dreamweaver",
                               "Enchanter",
                               "Illusionist",
                               "Medusa",
                               "Necromancer",
                               "Poisoner",
                               "Potion Master",
                               "Voodoo Master",
                               "Wilding"]

    def select_role(self, player):
        if not self.power_selected:
            if random.randint(1, 2) == 1:
                self.power_selected = True
                role = self.power[random.randint(0, len(self.power)-1)]
            else:
                role = self.everythingelse[random.randint(0, len(self.everythingelse)-1)]
                self.everythingelse.remove(role)
        if not self.killing_selected:
            if random.randint(1, 2) == 1:
                self.killing_selected = True
                role = self.killing[random.randint(0, len(self.killing)-1)]
            else:
                role = self.everythingelse[random.randint(0, len(self.everythingelse) - 1)]
                self.everythingelse.remove(role)


        else:
            role = self.everythingelse[random.randint(0, len(self.everythingelse) - 1)]
            self.everythingelse.remove(role)

        playerList.playerRoleList[player] = role


class Apoc:
    def __init__(self):
        self.roles = ["Soul Collector",
                               "Baker",
                               "Plaugebearer",
                               "Beserker",]

    def select_role(self, player):
            role = self.roles[random.randint(0, len(self.roles) - 1)]
            self.roles.remove(role)
            playerList.playerRoleList[player] = role

class Neutral:
    def __init__(self):
        self.evil = ["Pirate",
                     "Jester",
                     "Executioner",
                     "Amnesiac"]
        self.killing = ["Arsonist",
                        "Serial Killer",
                        "Werewolf",
                        "Shroud",
                        "Psychopath"]

    def select_role(self, player):
        if random.randint(1, 2) == 1:
            role = self.evil[random.randint(0, len(self.evil)-1)]
            self.evil.remove(role)

        else:
            role = self.killing[random.randint(0, len(self.killing)-1)]

        playerList.playerRoleList[player] = role

class Town:
    def __init__(self):
        self.power_count = 0
        self.power = ["Alchemist", "Jailor", "Marshal", "Mayor", "Monarch", "Prosecutor", "Duelist"]
        self.everythingelse = ["Admirer",
                               "Catalyst",
                               "Retributionist",
                               "Socialite",
                               "Tavern Keeper",
                               "Deputy",
                               "Trickster",
                               "Veteran",
                               "Vigilante"]

    def select_role(self, player):
        if self.power_count < 3:
            if random.randint(1, 3) == 1:
                role = self.power[random.randint(0, len(self.power)-1)]
                self.power.remove(role)
                self.power_count = self.power_count + 1
            else:
                role = self.everythingelse[random.randint(0, len(self.everythingelse)-1)]
        else:
            role = self.everythingelse[random.randint(0, len(self.everythingelse) - 1)]

        playerList.playerRoleList[player] = role