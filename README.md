# Aufgabe zwei


### Anforderungen an die Bibliothek:

In diesem Programm wird SHA256 (Secure hash algorithm 256) als Hash-Funktion verwendet. SHA256 ist sehr widerstandsfähig gegen Kollisionen. Wir würden sha256() der hashlib-Bibliothek verwenden, um die Implementierung der Funktion in Python zu nutzen. 

Das Modul hashlib ist in den meisten Python-Distributionen vorinstalliert. Wenn es in Ihrer Umgebung nicht vorhanden ist, können Sie das Modul mit folgendem Befehl in der Kommandozeile aufrufen.

##### ```pip install hashlib```

### Code-Erklärung:


Als Eingabe werden die Dateinamen (über ein Kommandozeilenargument) verwendet, daher müssen die Dateipfade über die Kommandozeile angegeben werden. Die Funktion hashfile() ist definiert, um mit beliebigen Dateigrößen umgehen zu können, ohne dass der Speicher knapp wird. Wenn wir alle Daten in einer Datei an die Funktion sha256.update() übergeben, werden die Daten nicht richtig gehasht, was zu Inkonsistenzen in den Ergebnissen führt. hashfile() gibt den Hash der Datei im base16 (hexadezimalen Format) zurück. Wir rufen dieselbe Funktion für beide Dateien auf und speichern ihre Hashes in zwei separaten Variablen. Danach werden die Hashes zum Vergleich herangezogen. Wenn beide Hashes gleich sind (d. h. die Dateien enthalten die gleichen Daten), geben wir die Meldung Beide Dateien sind gleich und dann den Hash aus. Wenn sie unterschiedlich sind, geben wir eine negative Meldung und den Hash der beiden Dateien aus (damit der Benutzer die unterschiedlichen Hashes visuell erkennen kann).

### Starten Sie das Programm:

Legen Sie zunächst beide Dateien dort ab, wo sich der Python-Code befindet. Später übergeben Sie beide Dateien beim Ausführen des Codes als Befehlszeilenargumente.


##### ```python <filename>.py <file1> <file2>```

##### Hinweis: Die obige Methode funktioniert für alle Dateiformate.



