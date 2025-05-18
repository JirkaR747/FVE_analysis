# Modul pro komponenty fotovoltaické elektrárny (FVE)
# Obsahuje třídy pro střídač, panely, konstrukci a baterie

from typing import Optional

# Třída střídače převádí stejnosměrný proud na střídavý
class Inverter:
    # Inicializace střídače s názvem, výkonem (kW) a cenou (Kč)
    def __init__(self, name: str, power: float, price: float) -> None:
        if power < 0 or price < 0:
            raise ValueError("Výkon i cena střídače musí být nezáporné")
        self.name = name
        self.power = power
        self.price = price

    # Vrátí cenu střídače
    def get_price(self) -> float:
        return self.price

# Třída fotovoltaických panelů představuje skupinu panelů
class PVModules:
    # Inicializace s názvem, výkonem jednoho panelu (W), cenou jednoho (Kč) a počtem kusů
    def __init__(self, name: str, power: float, unit_price: float, count: int) -> None:
        if power < 0 or unit_price < 0 or count < 0:
            raise ValueError("Výkon, cena ani počet panelů nesmí být záporné")
        self.name = name
        self.power = power
        self.unit_price = unit_price
        self.count = count

    # Vypočítá a vrátí celkovou cenu všech panelů
    def get_price(self) -> float:
        return self.unit_price * self.count

    # Vypočítá a vrátí celkový výkon všech panelů (W)
    def get_power(self) -> float:
        return self.power * self.count

# Třída konstrukce pro uchycení panelů na střeše či jiném povrchu
class Construction:
    # Inicializace s názvem konstrukce a její cenou (Kč)
    def __init__(self, name: str, price: float) -> None:
        if price < 0:
            raise ValueError("Cena konstrukce nesmí být záporná")
        self.name = name
        self.price = price

    # Vrátí cenu konstrukce
    def get_price(self) -> float:
        return self.price

# Třída jedné baterie s kapacitou a cenou
class Battery:
    # Inicializace s názvem, kapacitou (kWh) a cenou (Kč)
    def __init__(self, name: str, capacity: float, price: float) -> None:
        if capacity < 0 or price < 0:
            raise ValueError("Kapacita i cena baterie musí být nezáporné")
        self.name = name
        self.capacity = capacity
        self.price = price

    # Vrátí cenu baterie
    def get_price(self) -> float:
        return self.price

# Třída bateriového úložiště složeného z více baterií
class BatteryPack:
    # Inicializace s instancí Battery a počtem kusů
    def __init__(self, battery: Battery, pieces: int) -> None:
        if pieces < 0:
            raise ValueError("Počet baterií nesmí být záporný")
        self.battery = battery
        self.pieces = pieces

    # Přidá baterie do úložiště, kontrola kladného počtu
    def add_batteries(self, count: int) -> None:
        if count < 0:
            raise ValueError("Počet přidávaných baterií musí být kladný")
        self.pieces += count

    # Odebere baterie z úložiště, kontrola rozsahu
    def remove_batteries(self, count: int) -> None:
        if count < 0:
            raise ValueError("Počet odebíraných baterií musí být kladný")
        if count > self.pieces:
            raise ValueError(f"Není dostatek baterií k odebrání (max {self.pieces})")
        self.pieces -= count

    # Vrátí celkovou cenu všech baterií v úložišti
    def get_price(self) -> float:
        return self.battery.get_price() * self.pieces
