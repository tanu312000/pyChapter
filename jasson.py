import json
with open("/home/tanu/programs/pythonFiles/states.json")as f:
    data=json.load(f)
    for a in data["states"]:
        print(a)

