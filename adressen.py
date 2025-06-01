#!/usr/bin/env python3
from time import sleep
import os, ast
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromDictionary as cFD

versie = "0.25"
datum = "20250601"

basismap = os.path.dirname(os.path.realpath(__file__))
werkmap = basismap 
os.chdir(basismap)
with open("logo","r") as l:
    logo = ast.literal_eval(l.read())

colgoed = "\033[92m"
colslecht = "\033[91m"
col = "\033[95m"
col0 = "\033[0m"

veldenlijst = [
        "Voorna(a)m(en)",
        "Achterna(a)m(en)",
        "Organisatie",
        "Functie",
        "KvK",
        "BTW",
        "IBAN",
        "BIC",
        "BSN",
        "CF",
        "Verjaardag",
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
        "Aantekening",
        ]

maxlen = len(max(veldenlijst, key=len))
Optieslijst = [
        "Toevoegen",
        "Inzien",
        "Zoeken",
        "Wijzigen/Kopiëren",
        "Verwijderen",
        ]

ext = ".adr"
afsluitlijst = [":q","X","Q",":X",":Q"]
forlmax = ("{:<%d}" % maxlen).format
forr3 = "{:>3}".format
forr4 = "{:>4}".format
lijn = "-"*maxlen+"+"+"-"*maxlen
halflijn = "+"+"-"*maxlen
inputindent = "  : "

print(lijn)
for i in range(len(logo)):
    print(col+logo[i]+col0, end="", flush=True)
    sleep(0.001)
print(lijn
)
def printhidden():
    print("""  %s:q : Verlaten%s
  %s:u : Herstellen%s
  %s:w : Bevestigen%s
""" % (colslecht,col0,col,col0,colgoed,col0)
        )

printhidden()
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

def zoekadres():
    zoeken = True
    while zoeken == True:
        zoek = input("Geef een zoekterm op\n%s" % inputindent)
        if zoek == ":q":
            print(lijn)
            print(col+"Verlaten"+col0)
            exit()
        elif zoek == ":u":
            print(lijn)
            print(col+"Herstel"+col0)
            break
        lijstmetvelden = []
        for i in adressen:
            with open(i,"r") as a:
                adres = ast.literal_eval(a.read())
            for j,k in adres.items():
                if zoek.lower() in k.lower() and j not in lijstmetvelden:
                    lijstmetvelden.append(j)
        try:
            maxlenvelden = len(max(lijstmetvelden, key = len))
            formaxlenvelden = ("{:<%d}" % maxlenvelden).format
            for i in adressen:
                with open(i,"r") as a:
                    adres = ast.literal_eval(a.read())
                for j,k in adres.items():
                    if zoek.lower() in k.lower():
                        if zoek.lower() in k.lower():
                            print("%s is gevonden in %s" % (zoek,col+forlmax(i[:-4][:maxlen]))+col0+" : "+formaxlenvelden(j)+" : "+k)
        except:
            print("%s%s is niet gevonden%s" % (colslecht,zoek,col0))

def voorselectie():
    cijfersalfabet = ""
    for i in adressen:
        if i[0] not in cijfersalfabet:
            cijfersalfabet += i[0]
    while len(cijfersalfabet) > 0:
        gefilterd = input("Maak een voorselectie \"?\" of \"?:?\"\nKies uit %s\n%s" % (col+cijfersalfabet+col0,inputindent)).replace(" ","")
        if gefilterd == ":q":
            print(lijn)
            print(col+"Verlaten"+col0)
            exit()
        elif gefilterd == ":u":
            bereik = cijfersalfabet
            return bereik
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

def printadres(bereik):
    tony = True
    while tony == True:
        adresopties = []
        if bereik == None:
            break
        opties = []
        for i in adressen:
            if i[0] in bereik:
                adresopties.append(i[:-4])
        wat,uitvouw = cFNL([adresopties,"A",1,1,[":q",":u"]])
        if adresopties == []:
            break
        if uitvouw == ":q":
            print(lijn)
            print(col+"Verlaten"+col0)
            exit()
        elif uitvouw == ":u":
            print(lijn)
            print(col+"Herstel"+col0)
            break
        try:
            print(col+adresopties[uitvouw][:maxlen]+col0,end="")
            with open(adresopties[uitvouw]+".adr","r") as a:
                kenmerk = adresopties[uitvouw]
                adres = ast.literal_eval(a.read())
                print("-"*(maxlen-len(adresopties[uitvouw][:maxlen]))+halflijn)
                for j in veldenlijst:
                    if j in adres:
                        print(forlmax(j)+": "+adres[j])
            return kenmerk,adres
        except(Exception) as e:
            print(e)
            pass

def nieuwadres():
    printhidden()
    nieuw = {}
    for i in veldenlijst:
        nieuw[i] = ""
    nieuwloop = True
    while nieuwloop == True:
        wat,toevoegen = cFD([nieuw,1,veldenlijst[0],[":q",":u",":w"]])
        if toevoegen == ":q":
            print(lijn)
            print(col+"Verlaten"+col0)
            exit()
        elif toevoegen == ":u":
            print(lijn)
            print(col+"Herstel"+col0)
            break
        elif toevoegen == ":w":
            def kieskenmerk():
                print("Kies een veld als kenmerk of typ een nieuw")
                kenmerk,veld = cFD([nieuw,0,veldenlijst[0],[":q",":u"]])
                return kenmerk,veld
            kenmerk,veld = kieskenmerk()
            if kenmerk == ":q":
                exit()
            elif kenmerk == ":u":
                break
            check = True
            while check == True:
                if kenmerk+ext in adressen:
                    print("Er bestaat al een adres met dit kenmerk")
                    watnu,wat = cFNL([["Ander veld","Zelf typen"],"A",1,2,[":q"]])
                    if wat == ":q":
                        exit()
                    elif wat == 0:
                        kenmerk,veld = kieskenmerk()
                    else:
                        kenmerk = input(inputindent)
                else:
                    break
            with open(kenmerk+ext,"w") as n:
                print(nieuw,end="",file=n)
            break
        else:
            nieuw[toevoegen] = input(nieuw[toevoegen]+" : ")

def wijzigadres(bereik):
    wijzigloop = True
    while wijzigloop == True:
        adressenopties = []
        for i in bereik:
            for j in adressen:
                if j[0] == i:
                    adressenopties.append(j[:-4])
        adresoptie,optie = cFNL([adressenopties,"A",1,1,[":q",":u"]])
        if adresoptie == ":q":
            print(lijn)
            print(col+"Verlaten"+col0)
            exit()
        elif adresoptie == ":u":
            print(lijn)
            print(col+"Herstel"+col0)
            break    
        with open(adresoptie+ext,"r") as a:
            adres = ast.literal_eval(a.read())
        adresvelden = {}
        for i in veldenlijst:
            if i in adres:
                adresvelden[i] = adres[i]
            else:
                adresvelden[i] = ""
        wijzig = True
        while wijzig == True:
            printhidden()
            key,waarde = cFD([adresvelden,1,veldenlijst[0],[":q",":u",":w"]])
            if waarde == ":q":
                exit()
            elif waarde == ":u":
                break
            elif waarde == ":w":
                def kieskenmerk():
                    print("Kies een veld als kenmerk of typ een nieuw")
                    kenmerk,veld = cFD([adresvelden,0,veldenlijst[0],[":q",":u"]])
                    return kenmerk,veld
                kenmerk,veld = kieskenmerk()
                if kenmerk == ":q":
                    exit()
                elif kenmerk == ":u":
                    break
                kenmerkcheck = True
                while kenmerkcheck == True:
                    if kenmerk+ext in adressen:
                        print("Er bestaat al een adres met dit kenmerk")
                        watnu,wat = cFNL([["Ander veld","Overschrijven","Zelf typen"],"A",1,1,[":q",":u"]])
                        if wat == ":q":
                            exit()
                        if wat == ":u":
                            break
                        elif wat == 0:
                            kenmerk,veld = kieskenmerk()
                        elif wat == 2:
                            kenmerk = input("Kenmerk"+inputindent)
                    else:
                        break
                with open(kenmerk+ext,"w") as w:
                    for i in veldenlijst:
                        if adresvelden[i] == "":
                            del adresvelden[i]
                    print(adresvelden,end="",file=w)
                wijzigloop = False
                wijzig = False
            else:
                ip = input(waarde+" : ")
                if ip == ":q":
                    exit()
                elif ip == ":u":
                    break
                else:
                    adresvelden[waarde] = ip

def verwijderadres(bereik):
    printhidden()
    adressenopties = []
    for i in bereik:
        for j in adressen:
            if j[0] == i:
                adressenopties.append(j[:-4])
    adresoptie,optie = cFNL([adressenopties,"A",1,1,[":q",":u"]])
    if adresoptie == ":q":
        print(col+"Verlaten"+col0)
        exit()
    elif adresoptie == ":u":
        print(col+"Herstel"+col0)
        pass
    else:
        with open(adresoptie+ext,"r") as a:
            adres = ast.literal_eval(a.read())
        try:
            adres[veldenlijst[0]]
        except:
            adres[veldenlijst[0]] = ""
        verwijderloop = True
        while verwijderloop == True:
            print(colslecht,end="")
            OK,NOK = cFD([adres,0,veldenlijst[0],[":q",":u",":w"]])
            print(col0,end="")
            if OK == ":q":
                exit()
            elif OK == ":w":
                os.remove(adresoptie+ext)
                break
            else:
                break

loop = True
while loop == True:
    adressen = adreslijst()
    wat,lezenofschrijven = cFNL([Optieslijst,"A",1,2,[":q",":v"]])
    if lezenofschrijven == ":q":
        print(lijn)
        print(col+"Verlaten"+col0)
        exit()
    elif lezenofschrijven == ":v":
        print(lijn)
        print(col+"Versie"+col0)
        printversie()
        print(lijn)
    elif lezenofschrijven == 0:
        print(lijn)
        print(col+wat+col0)
        nieuwadres()
        print(lijn)
    elif lezenofschrijven == 2:
        print(lijn)
        print(col+wat+col0)
        zoekadres()
        print(lijn)
    elif lezenofschrijven == 3:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        wijzigadres(bereik)
        print(lijn)
    elif lezenofschrijven == 4:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        verwijderadres(bereik)
        print(lijn)
    #elif lezenofschrijven == 1:
    else:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        printadres(bereik)
        print(lijn)
