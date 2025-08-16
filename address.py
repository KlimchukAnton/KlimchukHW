class Address:
    def __init__(self, index, city, streat, house, flat):
        self.index = index
        self.city = city
        self.streat = streat
        self.house = house
        self.flat = flat

    def __str__(self):
        return (f"{self.index}, {self.city}, {self.streat},"
               f"{self.house} - {self.flat}")