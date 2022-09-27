import random
import copy
from re import sub

class Timer():
    def __init__(self, days, hours, mins):
        self.mins = mins
        self.hours = hours
        self.days = days

    def display_time_spent(self):
        self.mins += 160
        if self.mins >= 60:
            self.hours += (self.mins // 60)
            self.mins = (self.mins % 60)
        if self.hours >= 24:
            self.days += (self.hours // 24)
            self.hours = (self.hours % 24)
        return print("Time spent: " + str(time_spent.days) + " days, " + str(time_spent.hours) + " hours, " + str(time_spent.mins) + " mins ")
      
class Artifact:
    def __init__(self, type, mainstat, artifact_substats):
        self.type = type
        self.mainstat = mainstat
        self.substat1 = artifact_substats[0]
        self.substat2 = artifact_substats[1]
        self.substat3 = artifact_substats[2]
        self.substat4 = artifact_substats[3]

    def generate_mainstat(type):
        mainstat = Mainstat("", 0)
        if type == types[0]:
            mainstat.primary = mainstats_flower[0]
            mainstat.primary_value = mainstats_flower_value[0]
            Artifact.removing_substat(substats[0])
        elif type == types[1]:
            mainstat.primary = mainstats_plume[0]
            mainstat.primary_value = mainstats_plume_value[0]
            Artifact.removing_substat(substats[1])
        elif type == types[2]:
            index = random.choice(range(len(list(mainstats_sands))))
            mainstat.primary = mainstats_sands[index]
            mainstat.primary_value = mainstats_sands_value[index]
            i = 0
            for x in substats:
                if x.secondary == mainstat.primary:
                    substats.remove(x)
                    break
                i += 1

        elif type == types[3]:
            index = random.choice(range(len(list(mainstats_goblet))))
            mainstat.primary = mainstats_goblet[index]
            mainstat.primary_value = mainstats_goblet_value[index]
            i = 0
            for x in substats:
                if x.secondary == mainstat.primary:
                    substats.remove(x)
                    break
                i += 1

        elif type == types[4]:
            index = random.choice(range(len(list(mainstats_circlet))))
            mainstat.primary = mainstats_circlet[index]
            mainstat.primary_value = mainstats_circlet_value[index]
            i = 0
            for x in substats:
                if x.secondary == mainstat.primary:
                    substats.remove(x)
                    break
                i += 1

        return mainstat 

    def removing_substat(substat):
        for x in substats:
            if x.secondary == substat.secondary:
                substats.remove(x)
    
    def generate_substat():
        substat = Substat("", 0)
        index = random.choice(range(len(list(substats))))
        substat.secondary = substats[index].secondary
        substat.secondary_value = substats[index].secondary_value
        return substat

    def upgrade_artifact(upgrade_substat):
        stat_roll = [1, 0.9, 0.8, 0.7]
        i = 0
        for x in artifact_substats: 
            if x.secondary == upgrade_substat.secondary:
                artifact_substats[i].secondary_value += (artifact_substats_copy[i].secondary_value * random.choice(list(stat_roll)))
                break
            i += 1
         
class Type:
    def __init__(self, name):
        self.name = name

types = ["Flower of Life", "Plume of Death", "Sands of Eon", "Goblet of Eonothem", "Circlet of Logos"]

class Mainstat:
    def __init__(self, primary, primary_value):
        self.primary = primary
        self.primary_value = primary_value

mainstats_flower = ["HP"] 
mainstats_flower_value = [4780] 
mainstats_plume = ["ATK"]
mainstats_plume_value = [311] 
mainstats_sands = ["HP(%)", "ATK(%)", "DEF(%)", "Elemental Mastery", "Energy Recharge(%)"]
mainstats_sands_value = [46.6, 46.6, 58.3, 186.5, 51.8] 
mainstats_goblet = ["HP(%)", "ATK(%)", "DEF(%)", "Elemental Mastery", "Elemental DMG Bonus(%)", "Physical DMG Bonus(%)"]
mainstats_goblet_value = [46.6, 46.6, 58.3, 186.5, 46.6, 58.3] 
mainstats_circlet = ["HP(%)", "ATK(%)", "DEF(%)", "Elemental Mastery", "Crit Rate(%)", "Crit DMG(%)", "Healing Bonus(%)"]
mainstats_circlet_value = [46.6, 46.6, 58.3, 186.5, 31.1, 62.2, 35,9] 

class Substat:
    def __init__(self, secondary, secondary_value):
        self.secondary = secondary
        self.secondary_value = secondary_value

substat_hp = Substat("HP", 298.75)
substat_atk = Substat("ATK", 19.45)
substat_def = Substat("DEF", 23.15)
substat_hp_percentage = Substat("HP(%)", 5.83)
substat_atk_percentage = Substat("ATK(%)", 5.83)
substat_def_percentage = Substat("DEF(%)", 7.29)
substat_elemental_mastery = Substat("Elemental Mastery", 23.31)
substat_energy_recharge_percentage = Substat("Energy Recharge(%)", 6.48)
substat_crit_rate_percentage = Substat("Crit Rate(%)", 3.89)
substat_crit_dmg_percentage = Substat("Crit DMG(%)", 7.77)

substats = [substat_hp, substat_atk, substat_def, 
substat_hp_percentage, substat_atk_percentage, substat_def_percentage, 
substat_elemental_mastery, substat_energy_recharge_percentage, 
substat_crit_rate_percentage, substat_crit_dmg_percentage]


type = Type(random.choice(list(types)))
generate_mainstat = Artifact.generate_mainstat(type.name)
mainstat = Mainstat(generate_mainstat.primary, generate_mainstat.primary_value)

artifact_substats = []
generate_substat = Artifact.generate_substat()
substat1 = Substat(generate_substat.secondary, generate_substat.secondary_value)
artifact_substats.append(substat1)
Artifact.removing_substat(substat1)

generate_substat = Artifact.generate_substat()
substat2 = Substat(generate_substat.secondary, generate_substat.secondary_value)
artifact_substats.append(substat2)
Artifact.removing_substat(substat2)

generate_substat = Artifact.generate_substat()
substat3 = Substat(generate_substat.secondary, generate_substat.secondary_value)
artifact_substats.append(substat3)
Artifact.removing_substat(substat3)

generate_substat = Artifact.generate_substat()
substat4 = Substat(generate_substat.secondary, generate_substat.secondary_value)
artifact_substats.append(substat4)
Artifact.removing_substat(substat4)

artifact_substats_copy = copy.deepcopy(artifact_substats) 

Artifact.upgrade_artifact(random.choice((list(artifact_substats))))
Artifact.upgrade_artifact(random.choice((list(artifact_substats))))
Artifact.upgrade_artifact(random.choice((list(artifact_substats))))
Artifact.upgrade_artifact(random.choice((list(artifact_substats))))
Artifact.upgrade_artifact(random.choice((list(artifact_substats))))

artifact = Artifact(type, mainstat, artifact_substats)

print("Artifact Type: " + artifact.type.name + "\n" 
"Artifact Mainstat: " + artifact.mainstat.primary + ", Value: " + str(artifact.mainstat.primary_value) + "\n"
"Artifact Substats: " + artifact.substat1.secondary + ", Value: " + str(artifact.substat1.secondary_value) + "\n"
"                   " + artifact.substat2.secondary + ", Value: " + str(artifact.substat2.secondary_value) + "\n"
"                   " + artifact.substat3.secondary + ", Value: " + str(artifact.substat3.secondary_value) + "\n"
"                   " + artifact.substat4.secondary + ", Value: " + str(artifact.substat4.secondary_value))
time_spent = Timer(0, 0, 0)
Timer.display_time_spent(time_spent)