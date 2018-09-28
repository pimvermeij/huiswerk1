def standaardPrijs(afstandKM):
    'berkent de prijs door middel van de afstand als float'
    if afstandKM < 50:
        prijs = afstandKM * 0.8
    elif afstandKM <= 0:
        prijs = 0
    elif afstandKM >= 50:
        prijs = 15 + (afstandKM * 0.6)
    return prijs
def ritprijs(leeftijd, weekendrit, afstandKM):
    'berekent de ritprijs incl. korting met leeftijd als int, weekendrit als ja of nee en afstandKM als int'
    if (leeftijd < 12 or leeftijd >= 65) and weekendrit == True:
        korting = standaardPrijs(afstandKM) * 0.65
    elif leeftijd < 12 or leeftijd >= 65:
        korting = standaardPrijs(afstandKM) * 0.7
    elif (leeftijd >= 12 and leeftijd < 65) and weekendrit == True:
        korting = standaardPrijs(afstandKM) * 0.6
    else:
        korting = standaardPrijs(afstandKM)
    return korting
leeftijd = float(input("hoe oud ben je?"))
weekendrit = input ("is het weekend?")
afstandKM = float(input("wat is de afstand in kilometers?"))
if weekendrit == "ja":
    weekendrit = True
elif weekendrit == "nee":
    weekendrit = False
print(ritprijs(leeftijd, weekendrit, afstandKM))
