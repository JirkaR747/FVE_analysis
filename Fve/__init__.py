# Balíček Fve – rozhraní příkazového řádku pro správu FVE
# Zajišťuje menu, vstupy od uživatele a spouští hlavní logiku

import os
import sys
from typing import Optional

# Přidání adresáře s modulem do cesty hledání
sys.path.insert(0, os.path.dirname(__file__))

# Importy hlavních tříd a komponent
from FVE import FVE as FVEClass
from Fve_components import Inverter, PVModules, Construction, Battery, BatteryPack

# Funkce pro načtení desetinného čísla s kontrolou
def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Neplatná hodnota. Zadej číslo.")
        except KeyboardInterrupt:
            print("\nPřerušeno uživatelem.")
            raise

# Funkce pro načtení celého čísla s kontrolou
def prompt_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Neplatná hodnota. Zadej celé číslo.")
        except KeyboardInterrupt:
            print("\nPřerušeno uživatelem.")
            raise

# Funkce pro tvorbu instancí bez I/O
def create_fve(name: str) -> FVEClass:
    return FVEClass(name)

def create_inverter(name: str, power: float, price: float) -> Inverter:
    return Inverter(name, power, price)

def create_pv_modules(name: str, power: float, unit_price: float, count: int) -> PVModules:
    return PVModules(name, power, unit_price, count)

def create_construction(name: str, price: float) -> Construction:
    return Construction(name, price)

def create_battery_pack(name: str, capacity: float, price: float, pieces: int) -> BatteryPack:
    battery = Battery(name, capacity, price)
    return BatteryPack(battery, pieces)

# I/O vrstva pro interaktivní vstupy
def io_create_fve() -> FVEClass:
    nm = input("Zadej název FVE: ")
    return create_fve(nm)

def io_create_inverter() -> Inverter:
    nm = input("Název střídače: ")
    pw = prompt_float("Výkon (kW): ")
    pr = prompt_float("Cena (Kč): ")
    return create_inverter(nm, pw, pr)

def io_create_pv() -> PVModules:
    nm = input("Název panelů: ")
    pw = prompt_float("Výkon jednoho panelu (W): ")
    up = prompt_float("Cena jednoho panelu (Kč): ")
    cnt = prompt_int("Počet panelů: ")
    return create_pv_modules(nm, pw, up, cnt)

def io_create_construction() -> Construction:
    nm = input("Název konstrukce: ")
    pr = prompt_float("Cena konstrukce (Kč): ")
    return create_construction(nm, pr)

def io_create_battery_pack() -> BatteryPack:
    nm = input("Název baterie: ")
    cap = prompt_float("Kapacita baterie (kWh): ")
    pr = prompt_float("Cena baterie (Kč): ")
    cnt = prompt_int("Počet baterií: ")
    return create_battery_pack(nm, cap, pr, cnt)

# Zobrazení souhrnu FVE
def show_summary(fve: Optional[FVEClass]) -> None:
    if not fve:
        print("Neexistuje žádná FVE sestava. Nejprve ji vytvoř.")
        return
    print(f"\nFVE '{fve.name}':")
    print(f"  Celkový výkon: {fve.get_power():.2f} kWp")
    print(f"  Celková cena: {fve.get_price():,.0f} Kč")

# Hlavní smyčka nabídky aplikace
def main() -> None:
    fve: Optional[FVEClass] = None
    try:
        while True:
            print("\n=== FVE Management Menu ===")
            print("1) Vytvořit novou FVE sestavu")
            print("2) Přidat střídač")
            print("3) Přidat PV moduly")
            print("4) Přidat konstrukci")
            print("5) Přidat bateriové úložiště")
            print("6) Zobrazit přehled FVE")
            print("0) Konec aplikace")
            choice = input("Vyber možnost: ")

            if choice == "1":
                fve = io_create_fve()
            elif choice == "2":
                if not fve:
                    print("Nejdříve vytvoř FVE sestavu.")
                else:
                    fve.set_inverter(io_create_inverter())
            elif choice == "3":
                if not fve:
                    print("Nejdříve vytvoř FVE sestavu.")
                else:
                    fve.set_pv_modules(io_create_pv())
            elif choice == "4":
                if not fve:
                    print("Nejdříve vytvoř FVE sestavu.")
                else:
                    fve.set_construction(io_create_construction())
            elif choice == "5":
                if not fve:
                    print("Nejdříve vytvoř FVE sestavu.")
                else:
                    fve.set_battery_pack(io_create_battery_pack())
            elif choice == "6":
                show_summary(fve)
            elif choice == "0":
                print("Ukončuji aplikaci. Nashledanou!")
                break
            else:
                print("Neplatná volba, zkus to znovu.")
    except KeyboardInterrupt:
        print("\nUkončeno uživatelem. Nashledanou!")
    except Exception as ex:
        print(f"Neočekávaná chyba: {ex}")
        sys.exit(1)

# Spuštění hlavní funkce, pokud je modul volán jako skript
if __name__ == "__main__":
    main()
