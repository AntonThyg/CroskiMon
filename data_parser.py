import os
from objects.croskimon import Croskimon

def get_croskimon_list():
    directory = 'data/croskimons'
    try:
        entries = os.listdir(directory)
        
        files = [entry.split(".")[0] for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        return files
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def get_croskimon_from_json(name):
    directory = 'data/croskimons'
    if name not in get_croskimon_list():
        print(f"'{name}' not found in saved croskimon list.")
        return None

    file_path = os.path.join(directory, name + ".csv")
    croskimon: Croskimon

    try:
        with open(file_path, encoding='utf-8') as file:
            data = file.read()
            croskimon = Croskimon(data["name"], data["types"], data["stats"])
    except Exception as e:
        print(f"Failed to read croskimon file '{file_path}': {e}")
        return None

    return croskimon

#TODO: design save file layout.   
def save_game_state(name):
    directory = 'savedata/'
    try:
        os.makedirs(directory, exist_ok=True) 
        file_path = os.path.join(directory, (name or "default")+'.json')
        with open(file_path, 'w') as f:
            f.write({"name":name})

        print(f"Save file '{name}' created successfully in '{directory}'.")
    except Exception as e:
        print(f"Failed to create save file: {e}")

def delete_save(name):
    directory = 'savedata/'
    file_path = os.path.join(directory, name+'.csv')
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Failed to delete file '{name}': {e}")
