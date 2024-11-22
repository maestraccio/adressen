#!/usr/bin/env python3
from time import sleep
import os, ast

versie = "0.12"
datum = "20241122"

basismap = os.path.dirname(os.path.realpath(__file__))
werkmap = basismap 
os.chdir(basismap)
with open("logo","r") as l:
    logo = ast.literal_eval(l.read())

veldenlijst = [
        "Voorna(a)m(en)",
        "Achterna(a)m(en)",
        "Organisatie",
        "Functie",
        "KvK",
        "BTW",
        "IBAN",
        "BIC",
        "Adres",
        "Postcode",
        "Woonplaats",
        "Provincie",
        "Land",
        "Telefoon1",
        "Telefoon2",
        "Email1",
        "Email2",
        "Website1",
        "Website2",
        "Aantekening"
        ]
maxlen = len(max(veldenlijst, key=len))
optieeen = "  1 : Toevoegen"
optietwee = " >2 : Inzien"
optiedrie = "  3 : Zoeken"
optievier = "  4 : Wijzigen/Kopiëren"
optievijf = "  5 : Verwijderen"

col = "\033[95m"
col0 = "\033[0m"

ext = ".adr"
afsluitlijst = ["X","Q",":X",":Q"]
klaarlijst = ["OK"]
jalijst = ["J","Y"]
neelijst = ["N"]
forlmax = ("{:<%d}" % maxlen).format
forr3 = "{:>3}".format
lijn = "-"*maxlen+"+"+"-"*maxlen
halflijn = "+"+"-"*maxlen
inputindent = "  : "

print(lijn)
for i in range(len(logo)):
    print(col+logo[i]+col0, end="", flush=True)
    sleep(0.001)
print(lijn)

def printversie():
    print("Versie: %s, %s" % (versie,datum))

def adreslijst():
    adressen = []
    for a in os.listdir():
        if a[-4:] == ext:
            adressen.append(a)
    adressen = sorted(adressen)
    return adressen

def voorselectie():
    cijfersalfabet = ""
    for i in adressen:
        if i[0] not in cijfersalfabet:
            cijfersalfabet += i[0]
    while len(cijfersalfabet) > 0:
        gefilterd = input("Maak een voorselectie \"?\" of \"?:?\"\nKies uit %s\n%s" % (col+cijfersalfabet+col0,inputindent))
        if gefilterd.upper() in afsluitlijst:
            return
        if gefilterd == "":
            bereik = cijfersalfabet
            return bereik
        elif len(gefilterd) == 3 and gefilterd[1] == ":":
            voorbereik = gefilterd
        else:
            voorbereik = "%s:%s" % (gefilterd[0],gefilterd[0])
        if len(voorbereik) == 0:
            bereik = cijfersalfabet
        else:
            try:
                bereik = cijfersalfabet[cijfersalfabet.index(voorbereik[0]):cijfersalfabet.index(voorbereik[2])+1]
                print(bereik)
                return bereik
            except:
                print("Het bereik is hoofdlettergevoelig. Probeer het nog eens.")

def zoekadres():
    zoeken = True
    while zoeken == True:
        zoek = input("Geef een zoekterm op\n%s" % inputindent)
        if zoek.upper() in afsluitlijst:
            break
        for i in adressen:
            with open(i,"r") as a:
                adres = ast.literal_eval(a.read())
                for j,k in adres.items():
                    if zoek.lower() in k.lower():
                        print("%s is gevonden in %s" % (zoek,col+forlmax(i[:-4][:maxlen]))+col0+" : "+forlmax(j)+" : "+k)

def printadres():
    tony = True
    while tony == True:
        bereik = voorselectie()
        if bereik == None:
            break
        opties = []
        for i in adressen:
            if i[0] in bereik:
                print(forr3(adressen.index(i)+1)+" : "+col+i[:-4]+col0)
                opties.append(adressen.index(i))
        if opties == []:
            break
        uitvouwen = input("Inzien\n%s" % inputindent)
        if uitvouwen.upper() in afsluitlijst:
            break
        try:
            uitvouw = int(uitvouwen)-1
            print(col+adressen[uitvouw][:-4][:maxlen]+col0,end="")
            with open(adressen[uitvouw],"r") as a:
                kenmerk = adressen[uitvouw]
                adres = ast.literal_eval(a.read())
                print("-"*(maxlen-len(adressen[uitvouw][:-4][:maxlen]))+halflijn)
                for j in veldenlijst:
                    if j in adres:
                        print(forlmax(j)+": "+adres[j])
            print(lijn)
            return kenmerk,adres
        except:
            pass

def nieuwadres():
    nieuw = {}
    nieuwloop = True
    while nieuwloop == True:
        for i in veldenlijst:
            if i in nieuw:
                print(forr3(veldenlijst.index(i)+1)+" : "+forlmax(i)+" : "+nieuw[i])
            else:
                print(forr3(veldenlijst.index(i)+1)+" : "+forlmax(i))
        toevoegen = input("Kies een veld of \"OK\":\n%s" % inputindent)
        if toevoegen.upper() in afsluitlijst:
            break
        elif toevoegen.upper() in klaarlijst:
            kenmerkindex = 0
            for j in veldenlijst:
                kenmerkindex += 1
                if j in nieuw:
                    print(forr3(kenmerkindex)+" : "+forlmax(j)+": "+nieuw[j])
            kenmerk = input("Kies een veld als kenmerk of typ handmatig\n%s" % inputindent)
            oops = False
            try:
                if nieuw[veldenlijst[int(kenmerk)-1]]+ext in adressen:
                    print("Er bestaat al een adres met dit kenmerk")
                    oops = True
            except:
                if kenmerk+ext in adressen:
                    print("Er bestaat al een adres met dit kenmerk")
                    oops = True
            if oops == False:
                for i,j in nieuw.items():
                    if j == "":
                        nieuw = nieuw.pop(i,None)
                try:
                    with open(nieuw[veldenlijst[int(kenmerk)-1]]+ext,"w") as n:
                        print(nieuw,end="",file=n)
                    break
                except:
                    with open(kenmerk+ext,"w") as n:
                        print(nieuw,end="",file=n)
                    break
        try:
            toevoegen = int(toevoegen)-1
            if toevoegen not in range(len(veldenlijst)):
                pass
            else:
                nieuw[veldenlijst[toevoegen]] = input(veldenlijst[toevoegen]+" : ")
        except:
            pass

def wijzigadres():
    kenmerkadres = printadres()
    try:
        kenmerk = kenmerkadres[0]
        adres = kenmerkadres[1]
        wijzigloop = True
        while wijzigloop == True:
            for i in veldenlijst:
                if i in adres:
                    print(forr3(veldenlijst.index(i)+1)+" : "+forlmax(i)+" : "+adres[i])
                else:
                    print(forr3(veldenlijst.index(i)+1)+" : "+forlmax(i))
            toevoegen = input("Kies een veld of \"OK\":\n%s" % inputindent)
            if toevoegen.upper() in afsluitlijst:
                break
            elif toevoegen.upper() in klaarlijst:
                kenmerkindex = 0
                for j in veldenlijst:
                    kenmerkindex += 1
                    if j in adres:
                        print(forr3(kenmerkindex)+" : "+forlmax(j)+": "+adres[j])
                try:
                    waar = list(adres.keys())[list(adres.values()).index(kenmerk[:-4])]
                except:
                    waar = kenmerk[:-4]
                try:
                    kenny = input("Kies een veld als kenmerk (nu: %s)\n%s" % (str(veldenlijst.index(waar)+1)+" : "+col+kenmerk[:-4]+col0,inputindent))
                except:
                    kenny = input("Kies een veld als kenmerk (nu: %s)\n%s" % (col+kenmerk[:-4]+col0,inputindent))
                oops = False
                if kenny.upper() in afsluitlijst:
                    break
                elif kenny == "":
                    kenny = veldenlijst.index(waar)+1
                try:
                    if adres[veldenlijst[int(kenny)-1]]+ext in adressen and adres[veldenlijst[int(kenny)-1]]+ext != kenmerk:
                        print("Er bestaat al een adres met dit kenmerk")
                        oops = True
                except:
                    if kenny+ext in adressen and kenny+ext != kenmerk:
                        print("Er bestaat al een adres met dit kenmerk")
                        oops = True
                for i,j in adres.items():
                    if j == "":
                        adres = adres.pop(i,None)
                if oops == False:
                    try:
                        with open(adres[veldenlijst[int(kenny)-1]]+ext,"w") as w:
                            print(adres,end="",file=w)
                        break
                    except:
                        with open(kenny+ext,"w") as w:
                            print(adres,end="",file=w)
                        break
            try:
                toevoegen = int(toevoegen)-1
                if toevoegen not in range(len(veldenlijst)):
                    pass
                else:
                    adres[veldenlijst[toevoegen]] = input(veldenlijst[toevoegen]+" : ")
                    if adres[veldenlijst[toevoegen]] == "":
                        del adres[veldenlijst[toevoegen]]
            except:
                pass
    except:
        pass

def verwijderadres():
    verwijderloop = True
    while verwijderloop == True:
        bereik = voorselectie()
        if bereik == None:
            break
        opties = []
        for i in adressen:
            if i[0].upper() in bereik:
                print(forr3(adressen.index(i)+1)+" : "+col+i[:-4]+col0)
                opties.append(adressen.index(i)+1)
        weg = input("Welk adres wil je VERWIJDEREN?\n%s" % inputindent)
        if weg.upper() in afsluitlijst:
            break
        try:
            weg = int(weg)
            if weg not in opties:
                break
            else:
                definitief = input("Weet je zeker dat je %s wilt VERWIJDEREN?\n%s" % (col+adressen[weg-1][:-4]+col0,inputindent))
                if definitief.upper() not in jalijst:
                    break
                else:
                    os.remove(adressen[weg-1])
                    adressen.pop(weg-1)
                    return adressen
        except:
            pass

loop = True
while loop == True:
    adressen = adreslijst()
    lezenofschrijven = input("%s\n%s\n%s\n%s\n%s\n%s" % (optieeen,optietwee,optiedrie,optievier,optievijf,inputindent))
    if lezenofschrijven.upper() in afsluitlijst:
        exit()
    elif lezenofschrijven == "0":
        print(lijn)
        printversie()
        print(lijn)
    elif lezenofschrijven == "1":
        print(lijn)
        print(col+optieeen+col0)
        nieuwadres()
        print(lijn)
    elif lezenofschrijven == "3":
        print(lijn)
        print(col+optiedrie+col0)
        zoekadres()
        print(lijn)
    elif lezenofschrijven == "4":
        print(lijn)
        print(col+optievier+col0)
        wijzigadres()
        print(lijn)
    elif lezenofschrijven == "5":
        print(lijn)
        print(col+optievijf+col0)
        verwijderadres()
        print(lijn)
    #elif lezenofschrijven == "2":
    else:
        print(lijn)
        print(col+optietwee+col0)
        printadres()
