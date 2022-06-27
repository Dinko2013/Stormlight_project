from lib2to3.pytree import Base


class Character(Base):
      def __init__(self, name,year_born, year_died, bonded_with, birthplace,abilities,species,titles
                   ,profession,groups,nationality,planet,universe,books,ethnicity,spouse,relatives,
                   acestors,alias,residence,children):
        super().__init__(name,year_born,year_died)
        self.bonded_with = bonded_with
        self.birthplace =birthplace
        self.abilities = abilities
        self.species = species
        self.titles = titles
        self.profession = profession
        self.groups = groups
        self.nationality = nationality
        self.planet = planet
        self.universe = universe
        self.books = books
        self.ethnicity=ethnicity
        self.spouse=spouse
        self.relatives =relatives
        self.acestors =acestors
        self.alias =alias
        self.residence =residence
        self.children = children
        
        
        
        
        
        
