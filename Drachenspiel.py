def nehmen():
    anzahl = int(input("Wie viele nehmen Sie (1-3)? "))
    while anzahl < 1 or anzahl > 3:
        print("Der Drache schnauft: Nur 1, 2 oder 3 Münzen!")
        anzahl = int(input("Wie viele nehmen Sie (1-3)? "))
    return anzahl

coins = 21
print("Es liegen", coins, "Münzen im Hort.")

while coins > 1:
    coins -= nehmen()
    print("Jetzt liegen noch", coins, "Münzen im Hort.")
    if coins <= 1:
        print("Sie müssen die verfluchte Münze nehmen.")
        break

    coins -= 2
    print("Der Drache nimmt 2 Münzen.\nEs liegen noch", coins, "Münzen im Hort.")
