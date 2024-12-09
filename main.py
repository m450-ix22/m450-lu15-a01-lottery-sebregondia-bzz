from authenticate import login
from lottery import create_ticket
from menu import select_menu
from money import transfer_money


def main():
    print("Login erfolgreich!")
    while True:
        print("Lotto")
        print("---------")
        print("A) Konto Ein- und Auszahlungen tätigen")
        print("B) Lottotipps abgeben")
        print("Z) Beenden")
        choice = input("Option > ").upper()
        if choice == "Z":
            print("Programm beendet.")
            break
        elif choice == "A":
            print("Kontofunktion ausgewählt.")
        elif choice == "B":
            print("Lottotipps ausgewählt.")
        else:
            print("Ungültige Option. Bitte erneut wählen.")


if __name__ == '__main__':
    main()
