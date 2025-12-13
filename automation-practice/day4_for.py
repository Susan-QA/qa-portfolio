fruits = ["Apfel", "Banane", "Kiwi"]
        
for fruit in fruits:
    print(fruit)

print("")
        
items = ["Apfel", "Banane", 3, "Kiwi", "Ei"]

for item in items:
    if isinstance(item, str):
        print(item, "ist ein Text")
    else:
        print(item, "ist KEIN Text")
    
print("")
    
zahlen = [3, 117, 10, 25, 7, 40]

for zahl in zahlen:
    if zahl >= 10:
        print(zahl)
        
print("")

fruits = ["Apfel", "Banane", "Kirsche", "Orange", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, "-", fruit)
    
print("")
    
shopping_list = ["Eier", "Brot", "Butter", "Käse", "Wurst"]

for index, shop_item in enumerate(shopping_list, start=10):
    print(index, ":", shop_item)
    
print("")

numbers = [1, 5, 12, 7, 20, 3]
for num in numbers:
    if num >10:
        print(num)
        
print("")

shopping = ["Brot", "Milch", "Butter", "Käse"]

for index, shop_item in enumerate(shopping, start=1):
    print(index, "-", shop_item)
    
if "Milch" in shopping:
    print("Milch ist auf der Einkaufsliste vorhanden.")    
   
print("")

password = "abc123!"

for char in password:
    if char.isdigit():
        print("Das Passwort enthält mindestens eine Zahl.")
        break
