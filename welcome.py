import json


def save_data(data):
    with open("user_config.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def load_data():
    try:
        with open("user_config.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        data['visits'] += 1
        save_data(data)
        print(f"Welcome back, {data['namn']}! This is your visit number {data['visits']}.")
        return data
    
    
      
    
    
    except FileNotFoundError:
        name = input("Ange ditt namn: ")
        info = {
                 "namn": name,
                "visits": 1
        }

    
        save_data(info)
        print("Welcome, " + name + "! This is your first visit.")
        return info

load_data()

       



   




