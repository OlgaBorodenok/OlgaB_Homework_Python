from address import Address
from mailing import Mailing

to_address = Address("454028", "Челябинск", "Кузнецова", "21", "39")
from_address = Address("190000", "Санкт-Петербург", "Бассейная", "8", "712")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=300,
    track="RB123456789CN"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")