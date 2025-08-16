from address import Address
from mailing import Mailing

to_address = Address("332057", "Хабаровск", "Ленина", "25", "5")
froam_address = Address("145632", "Краснодар", "Ленинградская", "85", "49")

mailing = Mailing("3320084548231", froam_address, to_address, 500)

print(mailing)