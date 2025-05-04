from tariff_item import TariffItem
# ==========================================
# Reprezentace distributora elektřiny
# ==========================================
class Distributor:
    def __init__(self, name, region_code):
        self.name = name                    # Název distributora (např. ČEZ, PRE, EG.D)
        self.region_code = region_code      # Kód oblasti
        self.regulated_items = []           # Seznam regulovaných položek (stanovených ERÚ)

    def add_regulated_item(self, name, value, unit, vat=21):
        # Přidá regulovanou položku (např. distribuční poplatek)
        self.regulated_items.append(TariffItem(name, value, unit, vat))

    def __str__(self):
        return f"Distributor: {self.name} ({self.region_code})"
