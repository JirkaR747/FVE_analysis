# Modul pro distributora elektřiny
# Spravuje regulované položky tarifu

from tariff_item import TariffItem

# Třída reprezentuje distributora s regulovanými položkami
class Distributor:
    # Inicializace s názvem a kódem oblasti
    def __init__(self, name: str, region_code: str) -> None:
        self.name = name
        self.region_code = region_code
        self.regulated_items: list[TariffItem] = []

    # Přidá jednu regulovanou položku tarifu
    def add_regulated_item(self, name: str, value: float, unit: str, vat: float = 21.0) -> None:
        if value < 0 or vat < 0:
            raise ValueError("Cena ani DPH nesmí být záporná")
        item = TariffItem(name, value, unit, vat)
        self.regulated_items.append(item)

    # Vrátí textovou reprezentaci distributora
    def __str__(self) -> str:
        return f"Distributor: {self.name} ({self.region_code})"
