from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy A", "+7(924)-123-65-58"),
    Smartphone("Apple", "Iphone16 Pro Max", "+7(914)-631-64-04"),
    Smartphone("Honor", "400 Pro", "+7(999)-594-28-58"),
    Smartphone("LG", "Global 8", "+7(914)-671-37-91"),
    Smartphone("Sony", "Xperia XZ1", "+7(909)-852-36-74")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
