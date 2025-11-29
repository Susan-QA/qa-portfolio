# test_example.py
# Ein einfacher QA-Test: Prüfen, ob ein String in einem Text enthalten ist

text = "QA Testing ist spannend!"
assert "QA Testing" in text, "Text enthält QA Testing nicht"
print("Test erfolgreich: QA Testing gefunden!")
