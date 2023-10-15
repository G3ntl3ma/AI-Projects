def readfile(datei):
        datei = open(datei)

        inhalt = datei.read()

        datei.close()

        liste = inhalt.split()

        inListe = []

        for zeile in liste:
            wert = zeile.split(",")

            vektor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            for i in range( 16 ):
                vektor[i] = float(wert[i])

            inListe.append( vektor )

        return inListe 

def readcsv(datei):
        datei = open(datei)

        inhalt = datei.read()

        datei.close()

        liste = inhalt.split()

        inListe = []

        for zeile in liste:
            wert = zeile.split(";")

            vektor = [0,0,0,0,0]

            for i in range( 5 ):
                vektor[i] = float(wert[i])

            inListe.append( vektor )

        return inListe 
