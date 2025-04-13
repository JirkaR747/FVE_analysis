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
    def set_inverter(self, inverter: Inverter) -> None:
        self.inverter = inverter

    # přidání nebo změna batterií
    def set_batteryPack(self, battery_pack: BatteryPack) -> None:
        self.battery_pack = battery_pack

    # přidání nebo změna pv panelů
    def set_pvmoduls(self, pv_moduls: PVModuls) -> None:
        self.pv_moduls = pv_moduls

    # přidání nebo změna střešní konstrukce

    def set_construction(self, construction: Construction) -> None:
        self.construction = construction

    # metoda pro výpočet a získání ceny fve
    def get_price_fve(self) -> float:
        return self.inverter.get_price() + self.battery_pack.get_price() + self.pv_moduls.get_price() + self.construction.get_price()

    def get_power_fve(self)->float:
        return self.pv_moduls.get_power()