#python train_data/ATTCK.py 
from mitreattack.stix20 import MitreAttackData
import json 

def read_data():
    mitre_attack_data = MitreAttackData("../attack-stix-data/enterprise-attack/enterprise-attack.json")

    techniques = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)
    technique_list = []

    for technique in techniques:
        technique_id = technique["external_references"][0]["external_id"] 
        name = technique["name"]  
        description = technique.get("description", "Adversaries")  
        technique_list.append({
            "id": technique_id,
            "name": name,
            "Adversaries": description,
        })
    with open("train_data/data.json","w") as file:
        json.dump(technique_list,file, indent=4)
        
def temp():
    
    with open("train_data/data.json","r") as file:
        data = json.load(file)

        with open("train_data/data.json","w") as file:
            json.dump(data,file, indent=4)
            
            
read_data()