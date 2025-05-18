# menu.py – víceúrovňové menu pro FVE projekt
from Fve.Fve_components import Inverter, PVModuls, Construction, Battery, BatteryPack
from Fve.FVE import FVE
from tariff import Tariff
from tariff_item import TariffItem
from distributor import Distributor
from project_saver import ProjectSaver

fve_list = []
tariff_list = []
distributor_list = []

def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Zadejte platné číslo.")
        except KeyboardInterrupt:
            print("❌ Přerušeno uživatelem, zkuste znovu.")

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Zadejte platé celé číslo.")
        except KeyboardInterrupt:
            print("❌ Přerušeno uživatelem, zkuste znovu.")

def get_input(prompt: str) -> str:
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("❌ Přerušeno uživatelem.")
        return ""

# ========================== MENU STRUCTURE ==========================

def main_menu():
    while True:
        print("\n==== HLAVNÍ MENU ====")
        print("1) Vyhodnotit FVE")
        print("2) Konfigurace systému")
        print("3) Ukončit a uložit")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            evaluate_menu()
        elif choice == "2":
            config_menu()
        elif choice == "3":
            save_and_exit()
            break
        else:
            print("❌ Neplatná volba, zkuste znovu.\n")

# === 1. Vyhodnocení FVE ===
def evaluate_menu():
    while True:
        print("\n--- Vyhodnocení FVE ---")
        print("1) Vybrat existující FVE k vyhodnocení")
        print("2) Zadat novou FVE")
        print("3) Zpět")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            if not fve_list:
                print("⚠️ Žádná FVE není uložená. Zadejte nejprve novou.")
                continue
            print_fve_list()
            idx = get_int("Vyber číslo FVE pro vyhodnocení: ") - 1
            if 0 <= idx < len(fve_list):
                evaluate_fve(fve_list[idx])
            else:
                print("❌ Neplatná volba.")
        elif choice == "2":
            fve = create_fve()
            if fve:
                fve_list.append(fve)
                evaluate_fve(fve)
        elif choice == "3":
            return
        else:
            print("❌ Neplatná volba, zkuste znovu.\n")

def evaluate_fve(fve):
    try:
        if not tariff_list:
            print("⚠️ Není k dispozici žádný tarif. Nejprve zadejte nebo načtěte tarif v konfiguraci.")
            return
        consumption = get_float("Zadejte roční spotřebu (MWh): ")
        generation = fve.get_power()
        print(f"\n🌞 FVE {fve.name} (výkon {generation} kW):\n")
        print("{:<30} {:>17} {:>17} {:>17}".format("Tarif", "Náklad bez FVE", "Náklad s FVE", "Úspora"))
        print("-"*85)
        for tariff in tariff_list:
            cost_before = tariff.annual_cost(consumption, with_vat=True)
            cost_after = tariff.annual_cost(max(0, consumption - generation), with_vat=True)
            savings = cost_before - cost_after
            print("{:<30} {:>17.2f} {:>17.2f} {:>17.2f}".format(
                tariff.name, cost_before, cost_after, savings))
        print()
    except Exception as e:
        print(f"❌ Chyba při vyhodnocení: {e}")

# === 2. Konfigurace systému ===
def config_menu():
    while True:
        print("\n--- Konfigurace systému ---")
        print("1) Správa FVE sestav")
        print("2) Správa distributorů")
        print("3) Správa tarifů")
        print("4) Zpět")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            fve_management_menu()
        elif choice == "2":
            distributor_management_menu()
        elif choice == "3":
            tariff_management_menu()
        elif choice == "4":
            return
        else:
            print("❌ Neplatná volba, zkuste znovu.\n")

# --- Podmenu FVE ---
def fve_management_menu():
    while True:
        print("\n--- Správa FVE sestav ---")
        print("1) Vypsat FVE sestavy")
        print("2) Přidat novou FVE sestavu")
        print("3) Upravit existující FVE sestavu")
        print("4) Smazat FVE sestavu")
        print("5) Zpět")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            print_fve_list()
        elif choice == "2":
            fve = create_fve()
            if fve:
                fve_list.append(fve)
                print("✅ FVE sestava byla přidána.")
        elif choice == "3":
            print_fve_list()
            idx = get_int("Zadej číslo FVE k úpravě: ") - 1
            if 0 <= idx < len(fve_list):
                fve = fve_list[idx]
                new_name = get_input(f"Nový název FVE ({fve.name}): ")
                if new_name:
                    fve.name = new_name
                print("✅ FVE aktualizována.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "4":
            print_fve_list()
            idx = get_int("Zadej číslo FVE k odstranění: ") - 1
            if 0 <= idx < len(fve_list):
                del fve_list[idx]
                print("🗑️ FVE smazána.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "5":
            return
        else:
            print("❌ Neplatná volba, zkuste znovu.")

# --- Podmenu distributorů ---
def distributor_management_menu():
    while True:
        print("\n--- Správa distributorů ---")
        print("1) Vypsat distributory")
        print("2) Přidat distributora")
        print("3) Upravit distributora")
        print("4) Smazat distributora")
        print("5) Zpět")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            print_distributor_list()
        elif choice == "2":
            distributor = create_distributor()
            if distributor:
                distributor_list.append(distributor)
                print("✅ Distributor přidán.")
        elif choice == "3":
            print_distributor_list()
            idx = get_int("Zadej číslo distributora k úpravě: ") - 1
            if 0 <= idx < len(distributor_list):
                distributor = distributor_list[idx]
                new_name = get_input(f"Nový název distributora ({distributor.name}): ")
                if new_name:
                    distributor.name = new_name
                print("✅ Distributor aktualizován.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "4":
            print_distributor_list()
            idx = get_int("Zadej číslo distributora k odstranění: ") - 1
            if 0 <= idx < len(distributor_list):
                del distributor_list[idx]
                print("🗑️ Distributor smazán.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "5":
            return
        else:
            print("❌ Neplatná volba, zkuste znovu.")

# --- Podmenu tarifů ---
def tariff_management_menu():
    while True:
        print("\n--- Správa tarifů ---")
        print("1) Vypsat tarify")
        print("2) Přidat nový tarif")
        print("3) Upravit tarif")
        print("4) Smazat tarif")
        print("5) Zpět")
        choice = get_input("Zvol možnost: ").strip()
        if choice == "1":
            print_tariff_list()
        elif choice == "2":
            tariff = create_tariff()
            if tariff:
                tariff_list.append(tariff)
                print("✅ Tarif byl přidán.")
        elif choice == "3":
            print_tariff_list()
            idx = get_int("Zadej číslo tarifu k úpravě: ") - 1
            if 0 <= idx < len(tariff_list):
                t = tariff_list[idx]
                new_name = get_input(f"Nový název tarifu ({t.name}): ")
                if new_name:
                    t.name = new_name
                # Možnost změnit distributora
                if distributor_list:
                    print_distributor_list()
                    d_idx = get_int("Zadej číslo distributora pro tento tarif: ") - 1
                    if 0 <= d_idx < len(distributor_list):
                        t.set_distributor(distributor_list[d_idx])
                        print("✅ Distributor přiřazen k tarifu.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "4":
            print_tariff_list()
            idx = get_int("Zadej číslo tarifu k odstranění: ") - 1
            if 0 <= idx < len(tariff_list):
                del tariff_list[idx]
                print("🗑️ Tarif smazán.")
            else:
                print("❌ Neplatné číslo.")
        elif choice == "5":
            return
        else:
            print("❌ Neplatná volba, zkuste znovu.")

# ===== Pomocné funkce =====
def print_fve_list():
    if not fve_list:
        print("⚠️ Žádné FVE sestavy nejsou uloženy.")
        return
    for i, fve in enumerate(fve_list, 1):
        try:
            print(f"{i}) {fve.name}, výkon {fve.get_power()} kW")
        except Exception as e:
            print(f"{i}) Chyba: {e}")

def print_tariff_list():
    if not tariff_list:
        print("⚠️ Žádné tarify nejsou uloženy.")
        return
    for i, t in enumerate(tariff_list, 1):
        print(f"{i}) {t.name} ({t.distributor.name if t.distributor else 'bez distributora'})")

def print_distributor_list():
    if not distributor_list:
        print("⚠️ Žádní distributoři nejsou uloženi.")
        return
    for i, d in enumerate(distributor_list, 1):
        print(f"{i}) {d.name}")

def create_fve():
    try:
        name = get_input("Název FVE: ")
        inverter_power = get_float("Výkon měniče (kW): ")
        inverter = Inverter(inverter_power)
        battery_capacity = get_float("Kapacita baterie (kWh): ")
        battery = Battery(battery_capacity)
        battery_count = get_int("Počet baterií: ")
        battery_pack = BatteryPack(battery, battery_count)
        pv_power = get_float("Výkon panelů (kWp): ")
        pvmodules = PVModuls(pv_power)
        construction_area = get_float("Velikost konstrukce (m2): ")
        construction = Construction(construction_area)
        return FVE(name, inverter, battery_pack, pvmodules, construction)
    except Exception as e:
        print(f"❌ Chyba při vytváření FVE: {e}")
        return None

def create_distributor():
    try:
        name = get_input("Název distributora: ")
        # Přidání regulovaných položek (možno rozšířit dle potřeby)
        regulated_items = []
        while True:
            add_item = get_input("Přidat regulovanou položku? (ano/ne): ").lower()
            if add_item != "ano":
                break
            item_name = get_input("  Název položky: ")
            value = get_float("  Hodnota: ")
            unit = get_input("  Jednotka (Kč/MWh nebo Kč/měsíc): ")
            vat = get_float("  DPH (%): ")
            regulated_items.append(TariffItem(item_name, value, unit, vat))
        return Distributor(name, regulated_items)
    except Exception as e:
        print(f"❌ Chyba při vytváření distributora: {e}")
        return None

def create_tariff():
    try:
        name = get_input("Název tarifu: ")
        supplier = get_input("Dodavatel: ")
        valid_from = get_input("Platnost od (YYYY-MM-DD): ")
        tariff = Tariff(name, supplier, valid_from)
        if distributor_list:
            print_distributor_list()
            d_idx = get_int("Zadej číslo distributora pro tento tarif: ") - 1
            if 0 <= d_idx < len(distributor_list):
                tariff.set_distributor(distributor_list[d_idx])
            else:
                print("❌ Neplatný distributor, pokračuji bez distributora.")
        else:
            print("⚠️ Žádný distributor není uložen, tarif bude bez distributora.")
        while True:
            add_item = get_input("Přidat položku do tarifu? (ano/ne): ").lower()
            if add_item != "ano":
                break
            item_name = get_input("  Název položky: ")
            value = get_float("  Hodnota: ")
            unit = get_input("  Jednotka (Kč/MWh nebo Kč/měsíc): ")
            vat = get_float("  DPH (%): ")
            tariff.add_item(item_name, value, unit, vat)
        return tariff
    except Exception as e:
        print(f"❌ Chyba při vytváření tarifu: {e}")
        return None

def save_and_exit():
    try:
        ProjectSaver().save(fve_list, tariff_list)
        print("💾 Projekt byl uložen. Nashledanou.")
    except Exception as e:
        print(f"❌ Chyba při ukládání: {e}")

if __name__ == "__main__":
    try:
        fve_list[:], tariff_list[:] = ProjectSaver().load()
    except Exception:
        fve_list, tariff_list = [], []
    main_menu()
