# Modul pro položku tarifu
# Obsahuje cenu, jednotku a výpočet ceny s DPH

# Třída reprezentující jednu položku tarifu
class TariffItem:
    # Inicializace s názvem, hodnotou, jednotkou a sazbou DPH (%)
    def __init__(self, name: str, value: float, unit: str, vat: float = 21.0) -> None:
        if value < 0 or vat < 0:
            raise ValueError("Cena ani sazba DPH nesmí být záporná")
        self.name = name
        self.value = value
        self.unit = unit
        self.vat = vat

    # Vypočítá cenu položky včetně DPH
    def price_with_vat(self) -> float:
        return self.value * (1 + self.vat / 100)

    # Převede položku do čitelného textu
    def __str__(self) -> str:
        return f"{self.name}: {self.value} {self.unit} + DPH {self.vat}%"
