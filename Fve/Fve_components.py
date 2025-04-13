# třídy pro jednotlivé komponenty na sestavení FVE


# třída pro střídač
class Inverter:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price

    def get_price(self) -> float:
        return self.price


# třída pro PV panel
class PVModuls:
    def __init__(self, name: str, power: float, price: float, count: int) -> None:
        self.name = name
        self.power = power
        self.price = price
        self.count = count

    def get_price(self) -> float:
        return self.price * self.count

    def get_power(self):
        return self.power * self.count


# třída pro  střešní konstrukci panel
class Construction:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price


# třída pro baterie
class Battery:
    def __init__(self, name: str, power: float, price: float) -> None:
        self.name = name
        self.power = power
        self.price = price

    def get_price(self) -> float:
        return self.price


# třída pro sestavení bateriového uložiště
class BatteryPack:
    def __init__(self, battery: Battery, pieces: int) -> None:
        self.battery = battery
        self.pieces = pieces

    # nastavení validace proměné pieces
    @property
    def pieces(self) -> int:
        return self._pieces

    # nastavení setteru pro pieces
    @pieces.setter
    def pieces(self, pieces: int) -> None:
        if pieces < 0:
            raise ValueError("Počet baterií nemůže být záporný")
        self._pieces = pieces

    # metoda pro přidání baterie do uložiště
    def add_battery(self, pieces: int) -> None:

        if pieces < 0:
            raise ValueError("Pro přidání baterie musíš zadat kladné číslo")
        self.pieces += pieces

    # metoda pro odebrání baterií z uložiště
    def remove_battery(self, pieces: int) -> None:

        if pieces < 0:
            raise ValueError("Pro odebrání baterie musíš zadat kladné číslo")

        if pieces > self.pieces:
            raise ValueError(f"Nelze odebrat {pieces} ks , k dispozici je pouze {self.pieces} ks")

        self.pieces -= pieces

    # metoda pro zjištění celkové ceny uložiště
    def get_price(self) -> float:
        return self.battery.get_price() * self.pieces
