from tariff_item import TariffItem

# ==========================================
# Kompletní tarif obchodníka + odkaz na distributora
# ==========================================
class Tariff:
    def __init__(self, name, supplier, valid_from, valid_to=None):
        self.name = name             # Název tarifu
        self.supplier = supplier     # Název dodavatele (obchodníka)
        self.valid_from = valid_from # Datum začátku platnosti
        self.valid_to = valid_to     # Datum konce platnosti (nepovinné)
        self.items = []              # Seznam neregulovaných položek (silová elektřina, obchodní poplatek...)
        self.distributor = None      # Odkaz na distributora (s regulovanými položkami)

    def set_distributor(self, distributor):
        # Přiřadí k tarifu konkrétního distributora
        self.distributor = distributor

    def add_item(self, name, value, unit, vat=21):
        # Přidá neregulovanou položku do tarifu
        self.items.append(TariffItem(name, value, unit, vat))

    def total_price_per_mwh(self, with_vat=False):
        # Spočítá celkovou cenu za MWh (neregulované + regulované složky)
        total = sum(
            item.price_with_vat() if with_vat else item.value
            for item in self.items if item.unit == "Kč/MWh"
        )
        if self.distributor:
            total += sum(
                item.price_with_vat() if with_vat else item.value
                for item in self.distributor.regulated_items if item.unit == "Kč/MWh"
            )
        return total

    def total_monthly_fees(self, with_vat=False):
        # Spočítá celkové měsíční poplatky (neregulované + regulované)
        total = sum(
            item.price_with_vat() if with_vat else item.value
            for item in self.items if item.unit == "Kč/měsíc"
        )
        if self.distributor:
            total += sum(
                item.price_with_vat() if with_vat else item.value
                for item in self.distributor.regulated_items if item.unit == "Kč/měsíc"
            )
        return total

    def annual_cost(self, consumption_mwh, with_vat=False):
        # Vypočítá roční náklady podle spotřeby a všech poplatků
        return self.total_price_per_mwh(with_vat) * consumption_mwh + self.total_monthly_fees(with_vat) * 12

    def list_items(self):
        # Vypíše položky tarifu + případné položky distributora
        print("--- Obchodní část ---")
        for item in self.items:
            print(item)
        if self.distributor:
            print("--- Regulovaná část (distributor) ---")
            for item in self.distributor.regulated_items:
                print(item)

    def __str__(self):
        dist = f" / {self.distributor.name}" if self.distributor else ""
        return f"{self.name} ({self.supplier}{dist}) - platnost od {self.valid_from}" + \
               (f" do {self.valid_to}" if self.valid_to else "")
