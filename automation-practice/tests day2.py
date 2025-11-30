# Listen: veränderbar, feste Reihenfolge, verschiedene Datentypen

fruits = ["Apfel", "Banane", "Kiwi"]

fruits.append("Orange")    # hinzufügen

print(fruits)              # ['Apfel', 'Banane', 'Kiwi', 'Orange']

fruits.remove("Banane")    # entfernen

print(fruits)              # ['Apfel', 'Kiwi', 'Orange']

len(fruits)                # FIXME Anzahl Elemente - funktioniert nicht, keine Ausgabe


# dictionary: speichert Daten in Schlüssel–Wert-Paaren

user = {
    "name": "Moni",
    "age": 30,
    "is_active": True
}

print(user["name"])        # Moni

user["age"] = 31           # ändern
user["city"] = "Coburg"    # hinzufügen

print(user["age"])         # 31
print(user["city"])        # Coburg


# if/elif/else: steuert den Programmfluss

age = 18

if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")  # Volljährig


x = 10

if x > 10:
    print("x ist größer als 10")

elif x == 10:
    print("x ist genau 10")

else:
    print("x ist kleiner als 10")    # x ist genau 10


temp = 22

if temp >= 30:
    print("Sehr heiß")
elif temp >= 20:
    print("Warm")
elif temp >= 10:
    print("Kühl")
elif temp >= 0:
    print("Kalt")
else:
    print("Sehr kalt")    # Warm
zahl = 49

if zahl > 100: 
    print ("Groß")
elif 50 <= zahl <= 100: 
    print ("Mittel")
elif 10 <= zahl < 50: 
    print ("Klein")
else: 
    print ("Mini")        # Klein


# Zahlenklassifizierung

print('   Programmanfang Zahlenklassifizierung')

zahl = -5

if zahl > 1000: 
    print("Sehr groß")
elif 500 <= zahl <= 1000: 
    print("Groß")
elif 100 <= zahl < 500: 
    print("Mittel")
elif 10 <= zahl < 100:
    print("Klein")    
else: 
    print("Sehr klein")

print('   Programmende Zahlenklassifizierung')


# Altersgruppen

print('   Programmanfang Altersgruppen')

age = int(input("Wie alt bis du: "))

if 0 <= age <= 2: 
    print("Baby")
elif 3 <= age <= 12: 
    print("Kind")
elif 13 <= age <= 17: 
    print("Teenager")
elif 18 <= age <= 64:
    print("Erwachsener")    
else: 
    print("Senior")

print('   Programmende Altersgruppen')


# Passwortstärke

print('   Programmanfang Passwortstärke')

password = input("Gib dein Passwort ein: ")
valuepw = len(password)
print("Passwortlänge ist: ")
print(valuepw)

if valuepw < 4: 
    print("Sehr schwach")
elif 4 <= valuepw <= 7: 
    print("Schwach")
elif 8 <= valuepw <= 11: 
    print("Gut")
else:
    print("Stark")    


print('   Programmende Passwortstärke')