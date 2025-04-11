# třída pro vytvoření FVE
from Fve.Fve_components import Inverter, BatteryPack, PVModuls, Construction


class FVE:
    # konstruktor umožní vytvořit objekt pouze s nazvem

    def __init__(self, name: str, inverter: Inverter = None, battery_pack: BatteryPack = None,
                 pv_moduls: PVModuls = None,
                 construction: Construction = None) -> None:
        self.name = name
        self.inverter = inverter
        self.battery_pack = battery_pack
        self.pv_moduls = pv_moduls
        self.construction = construction

    # přidání nebo změna invertoru
    def setInverter(self, inverter: Inverter) -> None:
        self.inverter = inverter

    # přidání nebo změna batterií
    def setBatteryPack(self, battery_pack: BatteryPack) -> None:
        self.battery_pack = battery_pack

    # přidání nebo změna pv panelů
    def setPVModuls(self, pv_moduls: PVModuls) -> None:
        self.pv_moduls = pv_moduls

    # přidání nebo změna střešní konstrukce

    def setConstruction(self, construction: Construction) -> None:
        self.construction = construction

    # metoda pro výpočet a získání ceny fve
    def getPriceFve(self) -> float:
        return self.inverter.getPrice() + self.battery_pack.getPrice() + self.pv_moduls.getPrice() + self.construction.getPrice()

    def getPowerFve(self)->float:
        return self.pv_moduls.getPower()