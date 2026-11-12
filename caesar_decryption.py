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

