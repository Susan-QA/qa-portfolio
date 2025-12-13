#  Kombination: Listen + Bedingungen

fruit = ["Apfel", "Banane", "Kirsche", "Orange", "Mango"]

print(f"Hier ist eine Liste meiner Lieblingsfrüchte: {fruit}")

fruit_new = input("Welches ist deine Lieblingsfrucht? ")

if fruit_new in fruit:
    print(f"Gratuliere! {fruit_new} steht schon auf der Liste!")
    
else:
    fruit.append(fruit_new)
    print(f"Ich habe {fruit_new} der Liste hinzugefügt.")
    
print(f"Hier ist die aktualisierte Liste: {fruit}")