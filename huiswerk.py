def toon_aantal_kluizen_vrij(filename):
    'toont aantal lege kluizen door aantal lege lijnen in kluizen.txt'
    infile = open(filename, 'r')
    linesList = infile.readlines()
    infile.close()

    return "er zijn nog" + " " + str(12 - len(linesList)) + " " +"kluizen vrij"

def nieuwe_kluis(filename):
    'vraagt een nieuw kluisnummer aan, vraagt om het wachtwoorden en zet die dan als duo naar kluizen.txt'
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines:
        content = line.split(";")
        kluisnummer = int(content[0])
        kluisnummers.remove(kluisnummer)
    infile.close()
    ww = input("voer uw wachtwoord in:")
    gegeven_kluisnummer = kluisnummers[0]
    outfile = open(filename, 'a')
    outfile.write(str(kluisnummers[0]) + ";" + ww + "\n")
    print("u heeft kluisnummer" + " " + str(gegeven_kluisnummer))
    return

def kluis_openen(filename):
    kluisnummer = input("wat is uw kluisnummer?")
    wachtwoord = input("wat is uw wachtwoord?")
    kluis = kluisnummer + ";" + wachtwoord + "\n"
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines:
        if line == kluis:
            return "Uw kluis is geopend."
    return "De combinatie klopt niet"

print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
waarde = int(input("kies een waarde:"))
if waarde == 1:
    print(toon_aantal_kluizen_vrij('kluizen.txt'))
elif waarde == 2:
    nieuwe_kluis('kluizen.txt')
elif waarde == 3:
    print(kluis_openen("kluizen.txt"))
else:
    print("kies een geldige waarde")
