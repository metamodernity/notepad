class Building:
    __year = None
    __city = None

    def __init__(self, year = None, city = "Samara"):
        self.year = year
        self.city = city
        self.get_info()
    def get_info(self):
        print("Year:", self.year, "City:", self.city)

class School(Building):
    pupisl = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self. pupisl = pupils

    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupisl)

class House(Building):
    pass

class Shop(Building):
    pass

school = School(100, 2000, "Samara")
house = House(2000)
shop = Shop(2000)
