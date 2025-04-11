# třídy pro jednotlivé komponenty na sestavení FVE


# třída pro střídač
class Inverter:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price


# třída pro PV panel
class PVModul:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price

# třída pro  střešní konstrukci panel
class Construction:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price


# třída pro baterie panel
class Battery:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price


# třída pro sestavení bateriového uložiště
class BatteryPack:
    def __init__(self, battery:Battery,pieces:int)->None:
        self.battery=battery
        self.pieces=pieces
        self.price=pieces*battery.price