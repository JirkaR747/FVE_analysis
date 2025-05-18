import os
import json
from typing import Tuple, List
from Fve.Fve_components import Inverter, PVModuls, Construction, Battery, BatteryPack
from Fve.FVE import FVE
from tariff import Tariff


class ProjectSaver:
    """
    Singleton pro ukládání a načítání seznamu FVE sestav a tarifů do/z JSON souboru.
    """
    _instance = None

    def __new__(cls, filepath: str = "project_data.json"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.filepath = filepath
        return cls._instance

    def save(self, fve_list: List[FVE], tariffs: List[Tariff]) -> None:
        data = {
            "fve": [
                {
                    "name": fve.name,
                    "inverter": vars(fve.inverter),
                    "battery": {
                        "name": fve.battery_pack.battery.name,
                        "capacity": fve.battery_pack.battery.capacity,
                        "price": fve.battery_pack.battery.price
                    },
                    "battery_count": fve.battery_pack.pieces,
                    "construction": vars(fve.construction),
                    "pvmodules": vars(fve.pv_modules)
                }
                for fve in fve_list
            ],
            "tarify": [
                {
                    "name": t.name,
                    "supplier": t.supplier,
                    "valid_from": t.valid_from.strftime("%Y-%m-%d") if t.valid_from else None,
                    "valid_to": t.valid_to.strftime("%Y-%m-%d") if getattr(t, "valid_to", None) else None,
                    "items": [
                        {"name": it.name, "value": it.value, "unit": it.unit, "vat": it.vat}
                        for it in t.items
                    ]
                }
                for t in tariffs
            ]

        }
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"💾 Data byla uložena do souboru {self.filepath}")

    def load(self) -> Tuple[List[FVE], List[Tariff]]:
        if not os.path.exists(self.filepath):
            return [], []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        fve_list = []
        for entry in data.get("fve", []):
            inv = Inverter(**entry["inverter"])
            bat = Battery(**entry["battery"])
            bat_pack = BatteryPack(bat, entry["battery_count"])
            cons = Construction(**entry["construction"])
            pv = PVModuls(**entry["pvmodules"])
            fve_list.append(FVE(entry["name"], inv, bat_pack, pv, cons))

        tariff_list = []
        for entry in data.get("tarify", []):
            t = Tariff(entry["name"], entry["supplier"], entry["valid_from"])
            for it in entry.get("items", []):
                t.add_item(it["name"], it["value"], it["unit"], it["vat"])
            tariff_list.append(t)

        print(f"📂 Data načtena z {self.filepath}")
        return fve_list, tariff_list
