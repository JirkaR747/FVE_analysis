# ==========================================
# Jednotlivá položka v tarifu
# ==========================================
class TariffItem:
    def __init__(self, name, value, unit, vat=21):
        self.name = name        # Název položky (např. "Silová elektřina")
        self.value = value      # Cena položky (číslo)
        self.unit = unit        # Jednotka (např. Kč/MWh nebo Kč/měsíc)
        self.vat = vat          # Sazba DPH v procentech (např. 21)

    def price_with_vat(self):
        # Vrací cenu včetně DPH
        return self.value * (1 + self.vat / 100)

    def __str__(self):
        return f"{self.name}: {self.value} {self.unit} + DPH {self.vat}%"
