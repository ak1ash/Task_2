#Author: Akash Ravishankar

import sys
import hashlib


def datein_vergleicher(datein):
    # Ein beliebiger (aber fester) Buffer
    # Größe (entsprechend ändern)
    MAX_BUFFER_SIZE = 655366

    # Initialisierung der Methode sha256()
    sha_methode = hashlib.sha256()

    # Öffnen der Datei, die als
    # das erste Kommandozeilenargument
    with open(datein, 'rb') as f:

        while True:

            # Lesen von Daten = BUF_SIZE aus
            # der Datei und speichert sie in einer
            # Variable
            daten = f.read(MAX_BUFFER_SIZE)

            # Wahr, wenn eof = 1
            if not daten:
                break

            # Übergabe dieser Daten an die sha256-Hash
            # Funktion (Aktualisieren der Funktion mit
            # diesen Daten)
            sha_methode.update(daten)

    # sha256.hexdigest() hasht alle Eingabedaten
    # Daten, die über sha256.update() an sha256() übergeben werden.
    # fungiert als Finalisierungsmethode, nach der
    # alle Eingabedaten gehasht werden hexdigest()
    # hasht die Daten und gibt die Ausgabe
    # im hexadezimalen Format
    return sha_methode.hexdigest()


# Aufruf der Funktion hashfile(), um Hashes der Dateien zu erhalten
# der Dateien zu erhalten, und das Ergebnis
# in einer Variablen
hash_datein1 = datein_vergleicher(sys.argv[1])
hash_datein2 = datein_vergleicher(sys.argv[2])

# Primitiver String-Vergleich, um
# zu prüfen, ob die beiden Hashes übereinstimmen oder nicht
if(hash_datein1 == hash_datein2):
    print("Beide Dateien sind gleich")
    print(f"Hash: {hash_datein1}")

else:
    print("Dateien sind anders!")
    print(f"Hash von Datei 1: {hash_datein1}")
    print(f"Hash von Datei 2: {hash_datein2}")