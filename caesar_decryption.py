funk = "Rpsptxp Xpwofyr opc Kpyeclwp: Opc Lrpye hlcepe spfep Lmpyo ty Clfx 404.Old Alddhzce wlfepe AJESZY3. Gtpw Rwünv!"

def decrypt(funk, shift):
    ergebnis = ""
    for zeichen in funk:
        if "A" <= zeichen <= "Z":
            ergebnis += chr((ord(zeichen) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= zeichen <= "z":
            ergebnis += chr((ord(zeichen) - ord("a") - shift) % 26 + ord("a"))
        else:
            ergebnis += zeichen
    return ergebnis

print(decrypt(funk, 11))

Eingabe = input("Bitte geben sie die zu verschlüsselnde Ausgabe ein.")
shift_user = input("Bitte geben se nun den Shift an.")

def encrypt(Eingabe, shift):
    ergebnis = ""
    for zeichen in Eingabe:
        if "A" <= zeichen <= "Z":
            ergebnis += chr((ord(zeichen) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= zeichen <= "z":
            ergebnis += chr((ord(zeichen) - ord("a") + shift) % 26 + ord("a"))
        else:
            ergebnis += zeichen
    return ergebnis

Eingabe = input("\nBitte geben Sie den zu verschlüsselnden Text ein:\n ")
shift_user = int(input("\nBitte geben Sie nun den Shift an:\n "))

print(encrypt(Eingabe, shift_user))

for schluessel in range(26):
    print(schluessel, decrypt(funk, schluessel))


def ist_deutsch(text):
    text = text.lower()
    return "agent" in text or "raum" in text or "passwort" in text

for schluessel in range(26):
    klartext = decrypt(funk, schluessel)
    if ist_deutsch(klartext):
        print(schluessel, klartext)


haeufigkeit = {}
for zeichen in funk.lower():
    if "a" <= zeichen <= "z":
        haeufigkeit[zeichen] = haeufigkeit.get(zeichen, 0) + 1

haeufigster = max(haeufigkeit, key=haeufigkeit.get)
schluessel = (ord(haeufigster) - ord("e")) % 26

print("Häufigster Buchstabe:", haeufigster, "-> Schlüssel:", schluessel)
print(decrypt(funk, schluessel))
