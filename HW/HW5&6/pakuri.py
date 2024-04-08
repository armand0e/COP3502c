class Pakuri:
    def __init__(self, species):
        # Initialize the pakuri object with species attribute
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    def get_species(self):
        # Returns the species of this critter
        return self.species

    def get_attack(self):
        # Returns the attack value for this critter
        return self.attack

    def get_defense(self):
        # Returns the defense value for this critter
        return self.defense

    def get_speed(self):
        # Returns the speed of this critter
        return self.speed

    def set_attack(self, new_attack):
        # Changes the attack value for this critter to new_attack
        self.attack = new_attack

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
        # Will evolve the critter as follows: a) double the attack; b) quadruple the defense; and c) triple the speed
