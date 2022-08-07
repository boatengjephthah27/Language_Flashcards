
import json



no_count = 0




def save():
    
    try:
        with open("passwords.json","r") as file:
            data_file = json.load(file)
            file_dict = {"no_count_fr" : data_file["no_count_fr"]} 
            data_file.update(file_dict)

    except FileNotFoundError:
        with open("passwords.json","w") as file:
            json.dump(file_dict, file, indent=3)

    else:
        with open("passwords.json","w") as file:
            data_file["no_count_fr"] += 1
            json.dump(data_file, file, indent=3)
            
            

def call_():
    try:
        with open("passwords.json","r") as file:
            data_file = json.load(file)

    except FileNotFoundError:
        with open("passwords.json","w") as file:
            file_dict = {"no_count_fr" : no_count} 
            json.dump(file_dict, file, indent=3)

    else:
        if "no_count_fr" in data_file:
            data_file["no_count_fr"]
            print(data_file["no_count_fr"])
    
        
            
save()
call_()