def standaardPrijs(afstandKM):
    if afstandKM < 50:
        prijs = afstandKM * 0.8
    elif afstandKM <= 0:
        prijs = 0
    elif afstandKM >= 50:
        prijs = 15 + (afstandKM * 0.6)
    return prijs
def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        standaardPrijs(afstandKM) * 0.65
    elif leeftijd < 12 or leeftijd >= 65:
        standaardPrijs(afstandKM) * 0.7
    elif leeftijd >= 12 and leeftijd < 65 and weekendrit == True:
        standaardPrijs(afstandKM) * 0.6
    else:
        standaardPrijs(afstandKM)
    print(standaardPrijs(afstandKM))
leeftijd = float(input("hoe oud ben je?"))
weekendrit = input ("is het weekend?")
afstandKM = float(input("wat is de afstand in kilometers?"))
if weekendrit == "ja":
    weekendrit = True
elif weekendrit == "nee":
    weekendrit = False
ritprijs(leeftijd, weekendrit, afstandKM)
print("hallo")
