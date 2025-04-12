# třídy pro jednotlivé komponenty na sestavení FVE


# třída pro střídač
class Inverter:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price

    def getPrice(self)->float:
        return self.price


# třída pro PV panel
class PVModuls:
    def __init__(self, name: str, power: float, price: float, count:int) -> None:
        self.name = name
        self.power = power
        self.price = price
        self.count=count

    def getPrice(self)->float:
        return self.price*self.count

    def getPower(self):
        return self.power*self.count

# třída pro  střešní konstrukci panel
class Construction:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def getPrice(self)->float:
        return self.price


# třída pro baterie panel
class Battery:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price

    def getPrice(self)->float:
        return self.price


# třída pro sestavení bateriového uložiště
class BatteryPack:
    def __init__(self, battery:Battery,pieces:int)->None:
        self.battery=battery
        self.pieces=pieces

    def getPrice(self)->float:
        return self.battery.getPrice()*self.pieces