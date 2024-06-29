Im Folgenden wird die Umsetzung der Schnupperaufgabe beschrieben.

# Eingesetzter Tech-Stack

- Für die Datenhaltung wird MongoDB verwendet
- Für das Backend wird Python eingesetzt
- Beim Frontend wurden HTML, CSS sowie JavaScript verwendet

## Persistenz

Für die Datenhaltung wird eine Datenbank mit zwei Collections angelegt. Die Benutzerdaten sind vordefiniert.

```
use homeoffice
db.user.insertOne({user: "user1", password: "pass1"})
db.createCollection("timeRecording")

```

## Backend

Wie oben bereits erwähnt, wird an dieser Stelle Python eingesetzt. Hierbei wurden folgende Schritte durchgeführt

- Erzeugen eines neuen Projekts mit PyCharme(IDE)
- Anlegen der Module
	- _main.py_				Eintrittspunkt und Starten des Web Servers
	- _routing.py_			Implementierung der Endpoints
	- _dbService.py_		Zugriff auf die Datenbank
	- _emailservice.py_		Funktionalität für den E-Mail Versand
	
Bemerkung: Die Module wurden in der oben angegebenen Reihenfolge implementiert. Zum Testen der Funktionalität wurde der Quellcode zunächst ohne Frontend direkt aufgerufen.

### Endpoints im Modul routing.py

Die ersten vier Funktionen bzw. Endpoints sind für das Rendern der HTML-Seiten vorgesehen. Das sind

- _/_ Führt einen Redirect zur Login-Seite
- _/login_ Rendert die Login-Seite
- _/startstop_ Rendert die StartStop-Seite
- _/overview_ Rendert die Übersicht-Seite

Die weiteren Funktionen fungieren als REST-Schnittstellen zwischen dem Back- und Frontend

- _/start_ REST-Endpoint fügt die Start-Uhrzeit in die Datenbank ein
- _/stop_ REST-Endpoint fügt die Stop-Uhrzeit in die Datenbank ein
- _/recdata/date_ REST-Endpoint gibt die Uhrzeiten in Abhängigkeit des Datums zurück

### Implementierung der Persistenzlogik(dbService.py)

- _get\_user_ Gibt einen Benutzer zurück, wird für die Authentifizierung verwendet
- _start_ Schreibt die Start-Uhrzeit in die Datenbank
- _stop_ Aktualisiert das Dokument mit der jeweiligen Start-Zeit
- _get\_rec\_data_ Gibt die Uhrzeiten für ein bestimmtes Datum zurück

Bemerkung: Hier wurde die Funktionalität erst einmal ebenfalls direkt, d.h. ohne Frontend getestet.

### Implementierung der Logik für den E-Mail Versand(emailService.py)

- Els Erstes wurde eine Konfigurationsdatei `config/config.json` für den E-Mail Versand mit notwendigen Daten angelegt. Darin sind folgende Daten enthalten

	- _server_ SMTP Servername
	- _port_ Port des Servers 
	- _from_ Sender der Nachricht
	- _to_ Empfänger(Personalbüro-Mail-Adresse)
	- _username_ Benutzername bei der Authentifizierung
	- _password_ Passwort des Benutzers
	
Durch den Aufruf von `init()` werden die Konfigurationsdaten geladen.

- `send_mail(subject, message)` versendet eine E-Mail, an den in `to` angegebene Adresse.

	- _subject_	Betreff
	- _message_ Nachricht

## Frontend

Das Frondend wurde anhand der in der Aufgabenstellung abgebildeten Fenster erstellt.

- HTML-Seiten im Ordner _templates_
	- layout.html (Master Page, die anderen Seiten werden von dieser Seite abgeleitet)
	- login.html
	- startstop.html
	- overview.html

- CSS im Ordner _static/css_
	- style.css

- Javascript im Ordner _static/js_
	- worker.js implementiert die Frontend-Logik, z.B. Aufrufe der REST-Schnittstelle
