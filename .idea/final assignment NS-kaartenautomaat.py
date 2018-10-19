stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]
def inlezen_beginstation(stations):
    while True:
        beginstation = input("wat is uw beginstation?")
        if beginstation not in stations:
            print("dit is geen geldig beginstation.")
        else:
            return beginstation

beginstation = inlezen_beginstation(stations)

def inlezen_eindstations(stations, beginstation):
    while True:
        eindstation = input("wat is uw eindstation?")
        if eindstation not in stations:
            print("dit is geen geldig eindstation.")
        elif stations.index(eindstation) < stations.index(beginstation):
            print("deze trein komt niet langs", eindstation)
        else:
            return eindstation

eindstation = inlezen_eindstations(stations,beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    afstand = stations.index(eindstation) - stations.index(beginstation)

    print("het beginstation", beginstation, "is het", str(stations.index(beginstation)+1) + "e", "station in het traject.")
    print("het eindstation", eindstation, "is het", str(stations.index(eindstation)+1) + "e", "stations in het traject.")
    print("de afstand bedraagd", str(afstand), "station(s).")
    print("de prijs van het kaartje is", str(afstand * 5), "euro")
    print("jij stapt in de trein in:", beginstation)
    for tussenstations in list(range(stations.index(beginstation) + 1, stations.index(eindstation))):
        print("-", stations[tussenstations], end=" ")
    print("\n" + "jij stapt uit in:", eindstation)
    return
omroepen_reis(stations,beginstation,eindstation)

