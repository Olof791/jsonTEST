import json

FILENAME = "notes.json"

def save_notes(notes: list[str]):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2, ensure_ascii=False)


def load_notes():
    try: 
        with open(FILENAME, "r", encoding="utf-8",) as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def main():
    notes = load_notes()

    while True:
        print("Vad vill du göra")
        print("1. Visa alla anteckningar")
        print("2. Lägg till en anteckning")
        print("3. Ta bort alla")
        print("4. Avsluta")
        choice = input("Välj ett alternativ: 1- 4 ")

        if choice == "1":
            print("\nDina anteckningar:")
            if not notes:
                print("Inga anteckningar hittades." )
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

        elif choice == "2":
            text = input("Skriv din anteckning: ")
            notes.append(text)
            save_notes(notes)
            print("Anteckningen har sparats.")

        elif choice == "3":
            notes.clear()
            save_notes(notes)
            print("Alla anteckningar har tagits bort.")

        elif choice == "4":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
     main()  


                    



