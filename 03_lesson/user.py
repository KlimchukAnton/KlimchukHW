class User:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

Anton = User("Anton", "Klimchuk")
Klimchuk = User("Klimchuk", "Anton")
Anton_Klimchuk = User("Anton", "Klimchuk")