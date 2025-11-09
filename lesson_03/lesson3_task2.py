from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79163456789"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79164567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79045678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79056789012"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79087890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")