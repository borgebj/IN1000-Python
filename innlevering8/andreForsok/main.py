from spillebrett import Spillebrett

def main():
    print("\n"*50)
    rader = int(input("Antall rader (bortover): "))
    kolonner = int(input("Antall kolonner (nedover): "))
    hovedbrett = Spillebrett(kolonner, rader)

    valg = ""
    while valg != "q":
        hovedbrett.tegnBrett()
        hovedbrett.oppdatering()

        valg = input("Valg: ")

# starte hovedprogrammet
main()