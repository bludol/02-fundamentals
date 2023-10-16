'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.6236 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def PadaniNaPlanete(planet, hmotnost):
    rychlost = 0
    if planet == 'zeme':
        rychlost = EARTH_GRAVITY * hmotnost
        planet = "planete zemi",

    elif planet == 'mesic':
        rychlost = MOON_GRAVITY * hmotnost
        planet = "mesici"

    print('rychlost padu koule je ', rychlost)

def sound_vs_light():
    cas = 0
    cas = SPEED_OF_LIGHT / SPEED_OF_SOUND
    print('Vzdálenost kterou svetlo ubehne za 1 sekund trva zvuku %g dnů' % (cas/86_400))