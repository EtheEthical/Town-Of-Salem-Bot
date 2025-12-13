import random
import playerList

class Coven:
    def __init__(self):
        self.power_selected = False
        self.power = ["Coven Leader", "Hex Master", "Witch"]
        self.everythingelse = ["Conjurer",
                               "Dreamweaver",
                               "Enchanter",
                               "Illusionist",
                               "Jinx",
                               "Medusa",
                               "Necromancer",
                               "Poisoner",
                               "Potion Master",
                               "Ritualist",
                               "Voodoo Master",
                               "Wilding"]

    def select_role(self, player):
        if not self.power_selected:
            if random.randint(1, 2) == 1:
                self.power_selected = False
                role = self.power[random.randint(0, len(self.power)-1)]
            else:
                role = self.everythingelse[random.randint(0, len(self.everythingelse)-1)]
                self.everythingelse.remove(role)
    
        else:
            role = self.everythingelse[random.randint(0, len(self.everythingelse) - 1)]
            self.everythingelse.remove(role)

        playerList.playerRoleList[player] = role

class Town:
    def __init__(self):
        self.power_count = 0
        self.power = ["Alchemist", "Jailor", "Marshal", "Mayor", "Monarch", "Prosecutor"]
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
