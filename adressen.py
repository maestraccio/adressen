#!/usr/bin/env python3
from time import sleep
from datetime import datetime, timezone
import os, ast, textwrap
from chooseFromNumberedList import chooseFromNumberedList as cFNL
from chooseFromNumberedList import chooseFromKeysList as cFKL
from chooseFromNumberedList import chooseFromDictionary as cFD

nu = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

versie = "1.01"
datum = "20250629"

basismap = os.path.dirname(os.path.realpath(__file__))
werkmap = basismap 
os.chdir(basismap)
with open("logo","r") as l:
    logo = ast.literal_eval(l.read())

colgoed = "\033[92m"
colslecht = "\033[91m"
colv = "\033[2m"
col = "\033[95m"
col0 = "\033[0m"

NlijstNL = ["Achternaam","Voornaam","Middelste naam","Aanhef","Achtervoegsel"]
ADRlijstaNL = ["","","Straat + nr (a)","Plaats      (a)","Provincie   (a)","Postcode    (a)","Land        (a)"]
ADRlijstpNL = ["","","Straat + nr (p)","Plaats      (p)","Provincie   (p)","Postcode    (p)","Land        (p)"]
ADRlijstwNL = ["","","Straat + nr (w)","Plaats      (w)","Provincie   (w)","Postcode    (w)","Land        (w)"]
vCarddictNL = {
        "FN"              :"Weergavenaam",
        "N"               :NlijstNL,
        "ORG"             :"Organisatie",
        "TITLE"           :"Functie",
        "BDAY"            :"Verjaardag",
        "ADR;TYPE=HOME"   :ADRlijstpNL,
        "ADR;TYPE=WORK"   :ADRlijstwNL,
        "ADR;TYPE=OTHER"  :ADRlijstaNL,
        "TEL;TYPE=HOME"   :"Telefoon  (pvé)",
        "TEL;TYPE=WORK"   :"Telefoon  (wrk)",
        "TEL;TYPE=CELL"   :"Telefoon  (mob)",
        "TEL;TYPE=OTHER"  :"Telefoon  (and)",
        "TEL;TYPE=PREF"   :"Telefoon  (fav)",
        "EMAIL;TYPE=HOME" :"E-mail    (pvé)",
        "EMAIL;TYPE=WORK" :"E-mail    (wrk)",
        "EMAIL;TYPE=OTHER":"E-mail    (and)",
        "EMAIL;TYPE=PREF" :"E-mail    (fav)",
        "URL;TYPE=HOME"   :"Website   (pvé)",
        "URL;TYPE=WORK"   :"Website   (wrk)",
        "URL;TYPE=OTHER"  :"Website   (and)",
        "URL;TYPE=PREF"   :"Website   (fav)",
        "NOTE"            :"Aantekening"
        }
vollijstNL = [
        vCarddictNL["FN"],
        "Naam",
        NlijstNL[0],
        NlijstNL[1],
        NlijstNL[2],
        NlijstNL[3],
        NlijstNL[4],
        vCarddictNL["ORG"],
        vCarddictNL["TITLE"],
        vCarddictNL["BDAY"],
        "Adres   (privé)",
        ADRlijstpNL[2],
        ADRlijstpNL[3],
        ADRlijstpNL[4],
        ADRlijstpNL[5],
        ADRlijstpNL[6],
        "Adres    (werk)",
        ADRlijstwNL[2],
        ADRlijstwNL[3],
        ADRlijstwNL[4],
        ADRlijstwNL[5],
        ADRlijstwNL[6],
        "Adres  (anders)",
        ADRlijstaNL[2],
        ADRlijstaNL[3],
        ADRlijstaNL[4],
        ADRlijstaNL[5],
        ADRlijstaNL[6],
        vCarddictNL["TEL;TYPE=HOME"],
        vCarddictNL["TEL;TYPE=WORK"],
        vCarddictNL["TEL;TYPE=CELL"],
        vCarddictNL["TEL;TYPE=OTHER"],
        vCarddictNL["TEL;TYPE=PREF"],
        vCarddictNL["EMAIL;TYPE=HOME"],
        vCarddictNL["EMAIL;TYPE=WORK"],
        vCarddictNL["EMAIL;TYPE=OTHER"],
        vCarddictNL["EMAIL;TYPE=PREF"],
        vCarddictNL["URL;TYPE=HOME"],
        vCarddictNL["URL;TYPE=WORK"],
        vCarddictNL["URL;TYPE=OTHER"],
        vCarddictNL["URL;TYPE=PREF"],
        vCarddictNL["NOTE"]
        ]
translijstNL = []
for i in vCarddictNL:
    translijstNL.append(vCarddictNL[i])
maxlen = len(max(ADRlijstpNL+ADRlijstwNL+NlijstNL+translijstNL, key=len))

ext = ".vCard"
extvcf = ".vcf"
afsluitlijst = [":x",":q",":X",":Q"]
def printafsluiten(): 
    print(lijn)
    print(col+"Afsluiten"+col0)
bevestiglijst = [":w",":W"]
def printbevestigd(): 
    print(lijn)
    print(col+"Bevestigd"+col0)
teruglijst = [":u",":U"]
def printterug(): 
    print(lijn)
    print(col+"Terug"+col0)
vlijst = [":v",":V"]
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
print(lijn)
def printhidden():
    print("""  %s:q : Afsluiten%s
  %s:u : Herstellen%s
  %s:w : Bevestigen%s"""
        % (colslecht,col0,col,col0,colgoed,col0)
        )

printhidden()

def printversie():
    print("Versie: %s, %s" % (versie,datum))

def adreslijst():
    adressen = []
    for a in os.listdir():
        if a[-len(ext):].lower() == ext.lower():
            adressen.append(a)
    for a in os.listdir():
        if a[-len(extvcf):].lower() == extvcf.lower():
            adressen.append(a)
    adressen = sorted(adressen)
    return adressen

def zoekadres():
    zoeken = True
    while zoeken == True:
        zoek = input("Geef een zoekterm op (hoofdletterONgevoelig):\n%s" % inputindent)
        if zoek in afsluitlijst:
            printafsluiten()
            exit()
        elif zoek in teruglijst:
            printterug()
            break
        for x in adressen:
            keysvaluesdict = {}
            with open(x,"r") as a:
                lines = a.readlines()
                for l in lines:
                    try:
                        key = l[:l.index(":")]
                        value = l[l.index(":")+1:]
                        waarde = value.strip()
                        if key in vCarddictNL:
                            vCarddictNL[key] = waarde.strip()
                            if key == "N":
                                Nlijst = value.split(";")
                                for j in NlijstNL:
                                    keysvaluesdict[j] = Nlijst[NlijstNL.index(j)].strip()
                            elif key == "ADR;TYPE=HOME":
                                ADRplijst = value.split(";")
                                for j in ADRlijstpNL:
                                    keysvaluesdict[j] = ADRplijst[ADRlijstpNL.index(j)].strip()
                            elif key == "ADR;TYPE=WORK":
                                ADRwlijst = value.split(";")
                                for j in ADRlijstwNL:
                                    keysvaluesdict[j] = ADRwlijst[ADRlijstwNL.index(j)].strip()
                            elif key == "ADR;TYPE=OTHER":
                                ADRalijst = value.split(";")
                                for j in ADRlijstaNL:
                                    keysvaluesdict[j] = ADRalijst[ADRlijstaNL.index(j)].strip()
                    except:
                        pass
            for y,z in keysvaluesdict.items():
                if zoek.lower() in z.lower():
                    print("%s is gevonden in %s: %s: %s" % (zoek,col+x[:-len(ext)]+col0,forlmax(y),colgoed+z+col0))

def voorselectie():
    cijfersalfabet = ""
    for i in adressen:
        if i[0] not in cijfersalfabet:
            cijfersalfabet += i[0]
    while len(cijfersalfabet) > 0:
        gefilterd = input("Maak een voorselectie \"?\" of \"?:?\"\nKies uit %s\n%s" % (col+cijfersalfabet+col0,inputindent)).replace(" ","")
        if gefilterd in afsluitlijst:
            printafsluiten()
            exit()
        elif gefilterd in teruglijst:
            printterug()
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

def printeenadres(toon):
    print(lijn)
    try:
        if toon[-len(extvcf):].lower() == extvcf.lower():
            toon = toon[:-len(extvcf)]
        with open(toon+ext,"r") as a:
            llijst = []
            for l in a:
                if l[:l.index(":")] in vCarddictNL:
                    llijst.append(l[:l.index(":")])
        lenlijst = []
        for ll in llijst:
            lenlijst.append(vCarddictNL[ll])
        with open(toon+ext,"r") as a:
            for l in a:
                if l[:l.index(":")] in vCarddictNL:
                    if l[:l.index(":")] == "N":
                        Nlijst = l[l.index(":")+1:].split(";")
                    elif l[:l.index(":")] == "ADR;TYPE=HOME":
                        ADRlijstp = l[l.index(":")+1:].split(";")
                    elif l[:l.index(":")] == "ADR;TYPE=WORK":
                        ADRlijstw = l[l.index(":")+1:].split(";")
                    elif l[:l.index(":")] == "ADR;TYPE=OTHER":
                        ADRlijsta = l[l.index(":")+1:].split(";")
        ll = len(max(lenlijst+ADRlijstpNL+ADRlijstwNL+NlijstNL,key=len))
        with open(toon+ext,"r") as a:
            for l in a:
                if l[:l.index(":")] in vCarddictNL:
                    if l[:l.index(":")] == "FN":
                        print(col+("{:>%d}" % (ll+1+(len(l[l.index(":")+1:])/2))).format(l[l.index(":")+1:]),end=""+col0)
                    elif l[:l.index(":")] == "N":
                        print(colv+("{:>%d}" % (ll+1)).format("Naam|")+col0)
                        Nlijst = l[l.index(":")+1:].split(";")
                        for i in NlijstNL:
                            if Nlijst[NlijstNL.index(i)] == "":
                                pass
                            elif i == NlijstNL[-1] and Nlijst[NlijstNL.index(i)] == "\n":
                                break
                            elif i == NlijstNL[-1]:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+Nlijst[NlijstNL.index(i)],end="")
                            else:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+Nlijst[NlijstNL.index(i)])
                    elif l[:l.index(":")]  == "ADR;TYPE=HOME":
                        print(colv+("{:>%d}" % (ll+1)).format("Adres (privé)|")+col0)
                        ADRlijstp = l[l.index(":")+1:].split(";")
                        for i in ADRlijstpNL:
                            if ADRlijstp[ADRlijstpNL.index(i)] == "":
                                pass
                            elif i == ADRlijstpNL[-1] and ADRlijstp[ADRlijstpNL.index(i)] == "\n":
                                break
                            elif i == ADRlijstpNL[-1]:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijstp[ADRlijstpNL.index(i)],end="")
                            else:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijstp[ADRlijstpNL.index(i)])
                    elif l[:l.index(":")]  == "ADR;TYPE=WORK":
                        print(colv+("{:>%d}" % (ll+1)).format("Adres (werk)|")+col0)
                        ADRlijstw = l[l.index(":")+1:].split(";")
                        for i in ADRlijstwNL:
                            if ADRlijstw[ADRlijstwNL.index(i)] == "":
                                pass
                            elif i == ADRlijstwNL[-1] and ADRlijstw[ADRlijstwNL.index(i)] == "\n":
                                break
                            elif i == ADRlijstwNL[-1]:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijstw[ADRlijstwNL.index(i)],end="")
                            else:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijstw[ADRlijstwNL.index(i)])
                    elif l[:l.index(":")]  == "ADR;TYPE=OTHER":
                        print(colv+("{:>%d}" % (ll+1)).format("Adres (anders)|")+col0)
                        ADRlijsta = l[l.index(":")+1:].split(";")
                        for i in ADRlijstaNL:
                            if ADRlijsta[ADRlijstaNL.index(i)] == "":
                                pass
                            elif i == ADRlijstaNL[-1] and ADRlijsta[ADRlijstaNL.index(i)] == "\n":
                                break
                            elif i == ADRlijstaNL[-1]:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijsta[ADRlijstaNL.index(i)],end="")
                            else:
                                print(("{:%d}" % ll).format(i)+colv+"| "+col0+ADRlijsta[ADRlijstaNL.index(i)])
                    else:
                        wraptext = textwrap.wrap(l[l.index(":")+1:],80-ll-2)
                        print(("{:%d}" % ll).format(vCarddictNL[l[:l.index(":")]])+": "+wraptext[0])
                        if len(wraptext) > 1:
                            for i in wraptext[1:]:
                                print(("{:%d}" % ll).format("")+"  "+i)
    except(Exception) as e:
        #print(e)
        pass
    return toon

def printadres(bereik):
    adresopties = []
    if bereik == None:
        return
    opties = []
    for i in adressen:
        if i[0] in bereik:
            if i[-len(ext):].lower() == ext.lower():
                adresopties.append(i[:-len(ext)])
            elif i[-len(extvcf):].lower() == extvcf.lower():
                adresopties.append(i)
    wat,uitvouw = cFNL([adresopties,"A",1,1,afsluitlijst+bevestiglijst+teruglijst])
    if adresopties == []:
        return
    elif uitvouw in afsluitlijst:
        exit()
    elif uitvouw in teruglijst:
        return wat
    toon = adresopties[uitvouw]
    printeenadres(toon)
    return toon

def wijzigadres(bereik,now):
    wijzigkop = ["BEGIN:VCARD","VERSION:3.0"]
    wijzigvoet = "END:VCARD"
    wijzigdict = {}
    if now == 0:
        rauwtw = []
    else:
        tewijzigen = printadres(bereik)
        if tewijzigen in teruglijst:
            printterug()
            return
        with open(tewijzigen+ext,"r") as t:
            rauwtw = t.readlines()
    twrauw = {}
    for i in rauwtw:
        twrauw[i[:i.index(":")]] = i[i.index(":")+1:].strip()
    veldenlijst = []
    waardenlijst = []
    for i in twrauw:
        if i in ["BEGIN","VERSION","REV","UID"]:
            pass
        elif "X-ABLABEL" in i:
            pass
        elif i == "END":
            break
        elif i == "N":
            N = twrauw[i].split(";")
            for j in NlijstNL:
                veldenlijst.append(j)
                waardenlijst.append(N[NlijstNL.index(j)])
        elif "ADR" in i:
            if i == "ADR;TYPE=HOME":
                Ap = twrauw[i].split(";")
                for j in ADRlijstpNL:
                    veldenlijst.append(j)
                    waardenlijst.append(Ap[ADRlijstpNL.index(j)])
                if "PREF" in i:
                    for j in ADRlijstpfNL:
                        veldenlijst.append(j)
                        waardenlijst.append(Ap[ADRlijstpNL.index(j)])
            elif i == "ADR;TYPE=WORK":
                Aw = twrauw[i].split(";")
                for j in ADRlijstwNL:
                    veldenlijst.append(j)
                    waardenlijst.append(Aw[ADRlijstwNL.index(j)])
            else:
                Aa = twrauw[i].split(";")
                for j in ADRlijstaNL:
                    veldenlijst.append(j)
                    waardenlijst.append(Aa[ADRlijstaNL.index(j)])
        elif "EMAIL" in i:
            if i == "EMAIL":
                try:
                    vCarddictNL["EMAIL;TYPE=HOME"]
                    veldenlijst.append(vCarddictNL["EMAIL;TYPE=WORK"])
                    waardenlijst.append(twrauw[i])
                except:
                    veldenlijst.append(vCarddictNL["EMAIL;TYPE=HOME"])
                    waardenlijst.append(twrauw[i])
            elif "PREF" in i:
                veldenlijst.append(vCarddictNL["EMAIL;TYPE=PREF"])
                waardenlijst.append(twrauw[i])
            elif "ITEM" in i:
                veldenlijst.append(vCarddictNL["EMAIL;TYPE=OTHER"])
                waardenlijst.append(twrauw[i])
            else:
                veldenlijst.append(vCarddictNL[i])
                waardenlijst.append(twrauw[i])
        elif "TEL" in i:
            if i == "TEL":
                try:
                    vCarddictNL["TEL;TYPE=HOME"]
                    veldenlijst.append(vCarddictNL["TEL;TYPE=WORK"])
                    waardenlijst.append(twrauw[i])
                except:
                    veldenlijst.append(vCarddictNL["TEL;TYPE=HOME"])
                    waardenlijst.append(twrauw[i])
            elif "PREF" in i:
                veldenlijst.append(vCarddictNL["TEL;TYPE=PREF"])
                waardenlijst.append(twrauw[i])
            elif "ITEM" in i:
                veldenlijst.append(vCarddictNL["TEL;TYPE=OTHER"])
                waardenlijst.append(twrauw[i])
            else:
                veldenlijst.append(vCarddictNL[i])
                waardenlijst.append(twrauw[i])
        else:
            try:
                veldenlijst.append(vCarddictNL[i])
                waardenlijst.append(twrauw[i])
            except:
                pass
    for i in vollijstNL:
        if i in veldenlijst:
            wijzigdict[i] = waardenlijst[veldenlijst.index(i)]
        else:
            wijzigdict[i] = ""
    OS = False
    loop = True
    while loop == True:
        def mkvCard():
            lijst = wijzigkop+[]
            N = ""
            Ap = ";;"
            Aw = ";;"
            Aa = ";;"
            try:
                for i in NlijstNL:
                    N += wijzigdict[i]+";"
                N = N[:-1]
            except(Exception) as e:
                #print(e)
                pass
            try:
                for i in ADRlijstpNL[2:]:
                    Ap += wijzigdict[i]+";"
                Ap = Ap[:-1]
            except(Exception) as e:
                #print(e)
                pass
            try:
                for i in ADRlijstwNL[2:]:
                    Aw += wijzigdict[i]+";"
                Aw = Aw[:-1]
            except(Exception) as e:
                #print(e)
                pass
            try:
                for i in ADRlijstaNL[2:]:
                    Aa += wijzigdict[i]+";"
                Aa = Aa[:-1]
            except(Exception) as e:
                #print(e)
                pass
            for i in vCarddictNL:
                if i == "N":
                    if N == ";;;;":
                        pass
                    else:
                        lijst.append(i+":"+N)
                elif i == "ADR;TYPE=HOME":
                    if Ap == ";;;;;;":
                        pass
                    else:
                        lijst.append(i+":"+Ap)
                elif i == "ADR;TYPE=WORK":
                    if Aw == ";;;;;;":
                        pass
                    else:
                        lijst.append(i+":"+Aw)
                elif i == "ADR;TYPE=OTHER":
                    if Aa == ";;;;;;":
                        pass
                    else:
                        lijst.append(i+":"+Aa)
                elif vCarddictNL[i] in wijzigdict:
                    K = vCarddictNL[i]
                    if wijzigdict[K] == "":
                        pass
                    else:
                        lijst.append(i+":"+wijzigdict[K])
            lijst.append("REV:"+nu)
            lijst.append(wijzigvoet)
            vCard = ""
            for i in lijst:
                vCard += i+"\n"
            vCard = vCard.strip()
            return vCard
        lijst = []
        for i in wijzigdict:
            lijst.append(forlmax(i) + " : " + wijzigdict[i])
            if i == vCarddictNL["FN"]:
                print(col+wijzigdict[i]+col0)
        was,dat = cFNL([lijst,"A",1,2,afsluitlijst+bevestiglijst+teruglijst+vlijst])
        wat = was[:was.index(":")].strip()
        if dat == 1:
            was,dat = cFNL([lijst[2:7],"A",3,4,afsluitlijst+bevestiglijst+teruglijst+vlijst])
            wat = was[:was.index(":")].strip()
        elif dat == 10:
            was,dat = cFNL([lijst[11:16],"A",12,12,afsluitlijst+bevestiglijst+teruglijst+vlijst])
            wat = was[:was.index(":")].strip()
        elif dat == 16:
            was,dat = cFNL([lijst[17:22],"A",18,18,afsluitlijst+bevestiglijst+teruglijst+vlijst])
            wat = was[:was.index(":")].strip()
        elif dat == 22:
            was,dat = cFNL([lijst[23:28],"A",24,24,afsluitlijst+bevestiglijst+teruglijst+vlijst])
            wat = was[:was.index(":")].strip()
        if was in afsluitlijst:
            printafsluiten()
            exit()
        elif was in teruglijst:
            printterug()
            break
        elif was in vlijst:
            vCard = mkvCard()
            if wijzigdict[vCarddictNL["FN"]] == "":
                print(colslecht+"\"%s\" is leeg. Kan niet opslaan zonder \"%s\"" % (vCarddictNL["FN"],vCarddictNL["FN"])+col0)
            print(vCard)
        elif was in bevestiglijst:
            if wijzigdict[vCarddictNL["FN"]] == "":
                print(colslecht+"\"%s\" is leeg. Kan niet opslaan zonder \"%s\"" % (vCarddictNL["FN"],vCarddictNL["FN"])+col0)
            else:
                vCard = mkvCard()
                with open(wijzigdict["Weergavenaam"]+ext,"w") as v:
                    print(vCard, end = "", file = v)
        else:
            if was[was.index(":")+1:].strip() == "":
                print(was[:was.index(":")].strip())
            else:
                print(col+was+col0)
            dit = input()
            if dit in afsluitlijst:
                printafsluiten()
                exit()
            elif dit in teruglijst:
                pass
            elif dit+ext in adressen and OS == False:
                print("%s bestaat al!" % (colslecht+dit+col0))
                printeenadres(dit)
                print(lijn)
                overschrijven = input("%sBij opslaan zal bovenstaand worden overschreven!%s\nWil je toch de naam %s gebruiken?\n" % (colslecht,col0,col+dit+col0))
                if overschrijven in afsluitlijst:
                    printafsluiten()
                    exit()
                elif overschrijven in teruglijst:
                    pass
                elif overschrijven in bevestiglijst:
                    OS = True
                    wijzigdict[wat] = dit
            else:
                wijzigdict[wat] = dit

def verwijderadres(bereik):
    print(lijn)
    laatstgezien = printadres(bereik)
    printhidden()
    OK = input("Weet je zeker dat je %s wilt %sverwijderen%s?\n" % (colslecht+laatstgezien+col0,colslecht,col0))
    if OK in bevestiglijst:
        if laatstgezien[-len(extvcf):].lower() == extvcf.lower():
            os.remove(laatstgezien)
        else:
            os.remove(laatstgezien+ext)
        print("Daag, %s" % laatstgezien)

###############################################################################

loop = True
while loop == True:
    print(lijn)
    adressen = adreslijst()
    wat,lezenofschrijven = cFNL([["Toevoegen","Inzien","Zoeken","Wijzigen/Kopiëren","Verwijderen"],"A",1,2,afsluitlijst+bevestiglijst+teruglijst+vlijst])
    if lezenofschrijven in afsluitlijst+teruglijst:
        printafsluiten()
        exit()
    elif lezenofschrijven in vlijst:
        print(lijn)
        print(col+"Versie"+col0)
        printversie()
    elif lezenofschrijven == 0:
        print(lijn)
        print(col+wat+col0)
        wijzigadres("",0)
    elif lezenofschrijven == 2:
        print(lijn)
        print(col+wat+col0)
        zoekadres()
    elif lezenofschrijven == 3:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        wijzigadres(bereik,1)
    elif lezenofschrijven == 4:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        verwijderadres(bereik)
    #elif lezenofschrijven == 1:
    else:
        print(lijn)
        print(col+wat+col0)
        bereik = voorselectie()
        printadres(bereik)
