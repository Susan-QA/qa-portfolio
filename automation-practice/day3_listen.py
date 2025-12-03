#   Einkaufslisten-Manager

shopping = ["Brot", "Butter", "Milch"]

print("Aktuelle Einkaufsliste: ", shopping)

art_append = input("Bitte füge einen neuen Artikel zur Einkaufsliste hinzu: ")

shopping.append(art_append)

print("Aktualisierte Einkaufsliste: ", shopping)

art_remove = input("Welchen Artikel möchtest du entfernen? ")

shopping.remove (art_remove)

print("Aktualisierte Einkaufsliste: ", shopping)


#   Dictionary

user = {
    "name": "Moni",
    "job": "Sachbearbeitung",
    "city": "Coburg"
}

print("Aktuelle Benutzerdaten: ", user) 

user ["city"] = input("Bitte gib deine neue Stadt ein: ")

print("Aktualisierte Benutzerdaten: ", user)

user ["job"] = input("Bitte gib deinen neuen Job ein: ")

print("Aktualisierte Benutzerdaten: ", user)


#   Bedingungen (if/elif/else): Rabatt-Rechner

einkaufswert = int(input("Bitte gib den Einkaufswert ein: "))

if einkaufswert >= 200:
    rabatt_prozent = 20
elif 100 <= einkaufswert < 200:
    rabatt_prozent = 10
elif 50 <= einkaufswert < 100:
    rabatt_prozent = 5
else:
    rabatt_prozent = 0

print("Dein Rabatt beträgt: ", rabatt_prozent, "%")

neuer_preis = einkaufswert - (einkaufswert * rabatt_prozent / 100)

print("Dein neuer Preis nach Abzug des Rabatts ist: ", neuer_preis)