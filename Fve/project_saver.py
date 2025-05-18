import json
from typing import Any, Dict

class ProjectSaver:
    """
    Třída zajišťující uložení objektů projektu FVE, Tariff a Distributor do JSON souborů.
    """
    @staticmethod
    def save_fve(fve: Any, filepath: str) -> None:
        # Převod objektu FVE na dict a uložení do souboru
        data = ProjectSaver._serialize_fve(fve)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def save_tariff(tariff: Any, filepath: str) -> None:
        # Převod objektu Tariff na dict a uložení do souboru
        data = ProjectSaver._serialize_tariff(tariff)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def save_distributor(distributor: Any, filepath: str) -> None:
        # Převod objektu Distributor na dict a uložení do souboru
        data = ProjectSaver._serialize_distributor(distributor)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def _serialize_fve(fve: Any) -> Dict[str, Any]:
        # Sestavení slovníku z atributů FVE
        return {
            'name': fve.name,
            'inverter': {
                'name': fve.inverter.name,
                'power': fve.inverter.power,
                'price': fve.inverter.price
            },
            'battery_pack': {
                'battery': {
                    'name': fve.battery_pack.battery.name,
                    'power': fve.battery_pack.battery.power,
                    'price': fve.battery_pack.battery.price
                },
                'pieces': fve.battery_pack.pieces
            },
            'pv_modules': {
                'name': fve.pv_moduls.name,
                'power': fve.pv_moduls.power,
                'price': fve.pv_moduls.price,
                'count': fve.pv_moduls.count
            },
            'construction': {
                'name': fve.construction.name,
                'price': fve.construction.price
            }
        }

    @staticmethod
    def _serialize_tariff(tariff: Any) -> Dict[str, Any]:
        # Sestavení slovníku z atributů Tariff
        return {
            'name': tariff.name,
            'supplier': tariff.supplier,
            'valid_from': tariff.valid_from.isoformat(),
            'valid_to': tariff.valid_to.isoformat() if tariff.valid_to else None,
            'items': [
                {
                    'name': item.name,
                    'value': item.value,
                    'unit': item.unit,
                    'vat': item.vat
                } for item in tariff.items
            ],
            'distributor': {
                'name': tariff.distributor.name,
                'region_code': tariff.distributor.region_code
            } if tariff.distributor else None
        }

    @staticmethod
    def _serialize_distributor(distributor: Any) -> Dict[str, Any]:
        # Sestavení slovníku z atributů Distributor
        return {
            'name': distributor.name,
            'region_code': distributor.region_code,
            'regulated_items': [
                {
                    'name': item.name,
                    'value': item.value,
                    'unit': item.unit,
                    'vat': item.vat
                } for item in distributor.regulated_items
            ]
        }
