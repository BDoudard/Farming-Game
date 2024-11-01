
import random
is_day = True # Commence par le jour
day_count = 1 # Compte les jours passés
water = 0 # Quantité de pluie tombée
sun_days = 0 # Compte les jours ensoleillés 
money = 0 # Argent possédé par le joueur 
day_count_salary  = 0 # Compte les jours jusqu'au salaire du joueur




# Le joueur commence avec 2 unités de blé
player_ble = 2

# CYCLE JOURS ET NUITS
def change_day_night():
    global is_day, day_count
    if is_day:
        print(f"Le Soleil se lève. Début du jour {day_count}.")
        is_day = False
    else:
        print(f"Le jour {day_count} se termine. La nuit tombe.")
        day_count += 1
        is_day = True

        # pluie aléatoire
        global water, sun_days
        if random.choice([True, False]):
            water += 1
            print("Il commence à pleuvoir !")
        else:
            sun_days += 1
            print("Le temps est ensoleillé.")

    # somme d'argent tous les x tours
    global day_count_salary, money
    day_count_salary += 1
    if day_count_salary == 3:
        money += 150
        print(f"Vous recevez 150$. Vous avez {money}$")
        day_count_salary == 0 # remet le compteur de jours pour le salaire à 0


# DEFINITION D'UN VEGETAL ET DE SES BESOINS
class Vegetables:
    def __init__(self, name, seeds_needed, water_needed, sun_days, time_growth, localisation, hp, price):
        self.name = name
        self.seeds_needed = seeds_needed
        self.time_growth = time_growth
        self.water_needed = water_needed
        self.sun_days = sun_days
        self.localisation = localisation
        self.hp = hp
        self.price = price
        self.current_growth = 0 # Niveau de croissance actuel
        self.harvestable = False # Indique si la ressource peut être récoltée

    def growth(self, seeds, water, sun, time):
        if seeds >= self.seeds_needed and water >= self.water_needed and sun >= self.sun_days and time >= self.time_growth:
            self.current_growth += 1 # augmente la croissance
            print(f"{self.name} est en train de pousser. Croissance actuelle : {self.current_growth}/{self.time_growth}")
            if self.current_growth >= self.time_growth:
                self.harvestable = True # la ressource peut être récoltée
                print(f"{self.name} est prêt à être récolté !")
        else:
            print(f"{self.name} manque encore de ressource pour pousser.")

    def harvest(self):
        global player_ble
        if self.harvestable:
            player_ble += 1 # récolte 1 unité de blé
            print(f"Vous récoltez {self.name}.")
            print(f"Vous avez {player_ble} unité de {self.name}")
            return self.current_growth == 0 # remet la croissance à 0
            return self.harvestable == False # la ressource n'est plus récoltable
        else:
            print(f"{self.name} ne peut pas encore être récolté.")



# LES DIFFERENTS VEGETEAUX
BLE = Vegetables("Blé", 1, 2, 3, 2, "Campagne", 50, 1.5)
TOURNESOL = Vegetables("Tournesol", 4, 3, 5, 4, "Campagne", 40, 4)
SALADE = Vegetables("Salade", 1, 1, 2, 2, "Campagne", 35, 2.5)


# DEFINITION D'UN ANIMAL DE ET SES BESOINS
class Animals:
    def __init__(self, name, water_needed, food_needed, time_reproduce, localisation, hp, price):
        self.name = name
        self.water_needed = water_needed
        self.food_needed = food_needed
        self.time_reproduce = time_reproduce
        self.localisation = localisation
        self.hp = hp
        self.price = price 

# test cycle jours et nuits       
for _ in range(20):
    change_day_night()
    BLE.growth(player_ble, water, sun_days, day_count)
    if BLE.harvestable:
        BLE.harvest