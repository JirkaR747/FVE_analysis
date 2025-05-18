# Modul pro obchodní tarif a výpočet nákladů
# Spočítá cenu MWh, měsíční poplatky a roční náklady

from datetime import datetime, date
from typing import Optional
from tariff_item import TariffItem
from distributor import Distributor

# Třída reprezentuje tarif dodavatele
class Tariff:
    DATE_FORMAT = "%Y-%m-%d"

    # Inicializace s názvem, dodavatelem a platností (od-do)
    def __init__(self, name: str, supplier: str, valid_from: str, valid_to: Optional[str] = None) -> None:
        self.name = name
        self.supplier = supplier
        try:
            self.valid_from = datetime.strptime(valid_from, self.DATE_FORMAT).date()
        except ValueError:
            raise ValueError("valid_from musí být ve formátu YYYY-MM-DD")
        if valid_to:
            try:
                self.valid_to = datetime.strptime(valid_to, self.DATE_FORMAT).date()
            except ValueError:
             raise ValueError("valid_to musí být ve formátu YYYY-MM-DD")
        else:
            self.valid_to = None
        self.items: list[TariffItem] = []
        self.distributor: Optional[Distributor] = None

    # Přiřadí distributora k tarifu
    def set_distributor(self, distributor: Distributor) -> None:
        self.distributor = distributor

    # Přidá neregulovanou položku tarifu
    def add_item(self, name: str, value: float, unit: str, vat: float = 21.0) -> None:
        if value < 0 or vat < 0:
            raise ValueError("Cena ani DPH nesmí být záporná")
        item = TariffItem(name, value, unit, vat)
        self.items.append(item)

    # Spočítá cenu za MWh bez nebo s DPH
    def total_price_per_mwh(self, with_vat: bool = False) -> float:
        total = sum(
            (item.price_with_vat() if with_vat else item.value)
            for item in self.items if item.unit == "Kč/MWh"
        )
        if self.distributor:
            total += sum(
                (item.price_with_vat() if with_vat else item.value)
                for item in self.distributor.regulated_items if item.unit == "Kč/MWh"
            )
        return total

    # Spočítá měsíční poplatky bez nebo s DPH
    def total_monthly_fees(self, with_vat: bool = False) -> float:
        total = sum(
            (item.price_with_vat() if with_vat else item.value)
            for item in self.items if item.unit == "Kč/měsíc"
        )
        if self.distributor:
            total += sum(
                (item.price_with_vat() if with_vat else item.value)
                for item in self.distributor.regulated_items if item.unit == "Kč/měsíc"
            )
        return total

    # Spočítá roční náklady podle spotřeby (MWh) a DPH
    def annual_cost(self, consumption_mwh: float, with_vat: bool = False) -> float:
        if consumption_mwh < 0:
            raise ValueError("Spotřeba nesmí být záporná")
        return self.total_price_per_mwh(with_vat) * consumption_mwh + self.total_monthly_fees(with_vat) * 12

    # Textový popis tarifu včetně validity a distributora
    def __str__(self) -> str:
        dist = f" / {self.distributor.name}" if self.distributor else ""
        validity = f" do {self.valid_to}" if self.valid_to else ""
        return f"{self.name} ({self.supplier}{dist}) - od {self.valid_from}{validity}"
