from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        # Initializes this object to contain exactly capacity objects when completely full. The default capacity for
        # the pakudex should be 20
        self.capacity = capacity
        self.list = [] 
        

    def get_size(self):
        # Returns the number of critters currently being stored in the pakudex
        return len(self.list)

    def get_capacity(self):
        # Returns the number of critters that the pakudex has the capacity to hold at most
        return self.capacity

    def get_species_array(self):
        # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no
        # species added yet, this method should return None
        if len(self.list) == 0:
            return None
        else:
            # for every pakuri object in pakudex.list, get their species, and put it in a list
            species_list = []
            for pakuri in self.list:
                species_list.append(pakuri.get_species())
            return species_list

    def get_stats(self, species):
        # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1,
        # and 2 respectively; if species is not in the pakudex, returns None
        stat_list = []
        for pakuri in self.list:
            if species == pakuri.get_species():
                stat_list.append(pakuri.get_attack())
                stat_list.append(pakuri.get_defense())
                stat_list.append(pakuri.get_speed())
                return stat_list
        return None

    def sort_pakuri(self):
        # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
        # self.list = sorted(self.list, key=lambda pakuri: pakuri.get_species())
        self.list.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        # Adds species to the pakudex; if successful, return True, and False otherwise
        for pakuri in self.list:
            if species == pakuri.get_species():
                return False
        new_pakuri = Pakuri(species)
        self.list.append(new_pakuri)
        return True

    def evolve_species(self, species):
        # Attempts to evolve species within the pakudex; if successful, return True, and False otherwise
        for pakuri in self.list:
            if species == pakuri.get_species():
                pakuri.evolve()
                return True
        return False
