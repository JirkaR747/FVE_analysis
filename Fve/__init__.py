# zatím jen na zkoušku

from Fve.FVE import FVE
from Fve.Fve_components import Battery, Inverter, BatteryPack, Construction, PVModuls


try:
    inverter = Inverter("Dražice", 15, 54000)
    battery = Battery("Dražice", 3.1, 25000)
    battery_pack = BatteryPack(battery, 0)
    construction=Construction("Swan",54000)
    pv_modul=PVModuls("Yamoto",450,4200,24)
    fve=FVE("Dražice-Kudláček",inverter,battery_pack,pv_modul,construction)
    print(f'velikost fve je {fve.get_power_fve()} kWp a cena je {fve.get_price_fve()} KČ')

    battery_pack.add_battery(2)
    print(f'velikost fve je {fve.get_power_fve()} kWp a cena je {fve.get_price_fve()} KČ')

    battery_pack.remove_battery(3)
    print(f'velikost fve je {fve.get_power_fve()} kWp a cena je {fve.get_price_fve()} KČ')

except ValueError as ex:
    print(ex)