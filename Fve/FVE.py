# Modul pro celkovou fotovoltaickou elektrárnu (FVE)
# Agreguje komponenty do jednoho celku s výpočtem ceny a výkonu

from typing import Optional
from Fve_components import Inverter, PVModuls, Construction, BatteryPack

# Třída reprezentující kompletní FVE sestavu
class FVE:
    # Inicializace s názvem a volitelnými komponentami
    def __init__(
        self,
        name: str,
        inverter: Optional[Inverter] = None,
        battery_pack: Optional[BatteryPack] = None,
        pv_modules: Optional[PVModuls] = None,
        construction: Optional[Construction] = None
    ) -> None:
        self.name = name
        self.inverter = inverter
        self.battery_pack = battery_pack
        self.pv_modules = pv_modules
        self.construction = construction

    # Nastaví nebo změní střídač
    def set_inverter(self, inverter: Inverter) -> None:
        self.inverter = inverter

    # Nastaví nebo změní PV panely
    def set_pv_modules(self, pv_modules: PVModuls) -> None:
        self.pv_modules = pv_modules

    # Nastaví nebo změní konstrukci
    def set_construction(self, construction: Construction) -> None:
        self.construction = construction

    # Nastaví nebo změní bateriové úložiště
    def set_battery_pack(self, battery_pack: BatteryPack) -> None:
        self.battery_pack = battery_pack

    # Spočítá celkovou cenu FVE ze všech komponent
    def get_price(self) -> float:
        total = 0.0
        if self.inverter:
            total += self.inverter.get_price()
        if self.pv_modules:
            total += self.pv_modules.get_price()
        if self.battery_pack:
            total += self.battery_pack.get_price()
        if self.construction:
            total += self.construction.get_price()
        return total

    # Spočítá celkový výkon FVE (kWp) pouze z panelů
    def get_power(self) -> float:
        return self.pv_modules.get_power() if self.pv_modules else 0.0
