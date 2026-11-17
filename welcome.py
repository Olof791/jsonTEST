import json


def load_data():
    try:
        with open("user_config.jason", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

    def save_data(data):
        with open("user_config.jason", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    name = input("Ange ditt namn: ")

    info = {
        "namn": name,
        "visits": 1
    }

    data.append(info)
    save_data(data)
    print("Welcome, " + name + "! This is your first visit.")
    

