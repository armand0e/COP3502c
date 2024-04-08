from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity=20):
        self.capacity=20
        
        # Initializes this object to contain exactly capacity objects when completely full. The default capacity for the pakudex should be 20
    def get_size(self):
        # Returns the number of critters currently being stored in the pakudex
        return len(self)
    
    
    def get_capacity(self):
        # Returns the number of critters that the pakudex has the capacity to hold at most
        return self.capacity
    
    
    def get_species_array(self):
        # Returns a string list containing the species of the critters as ordered in the pakudex; if there are no species added yet, 
        # this method should return None
        if len(self) == 0:
            return None
        else:
            strlist = []
            for i in self:
                strlist.append(str(i.species))
            return strlist
    
    
    def get_stats(self, species):
        # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2 respectively; 
        # if species is not in the pakudex, returns None
        if species not in self:
            return None
        else:
            intlist = []
            for i in self:
                if i.species == species:
                    intlist.append(i.attack)
                    intlist.append(i.defense)
                    intlist.append(i.speed)
            return intlist

                    
            
    def sort_pakuri(self):
        # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
        self.sort()


    def add_pakuri(self, species):
        # Adds species to the pakudex; if successful, return True, and False otherwise
        new_pakuri = Pakuri(species)
        self.append(new_pakuri)
        
        
    def evolve_species(self, species):
        # Attempts to evolve species within the pakudex; if successful, return True, and False otherwise
        for i in self:
            if i.species == species:
                Pakudex.evolve()