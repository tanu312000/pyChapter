import json
with open("/home/tanu/programs/pythonFiles/states.json")as f:
    data=json.load(f)

    for a in data['states']:
        del a['name']
        del a['abbreviation']
        print(a)

        with open("/home/tanu/programs/pythonFiles/states2.json",'a')as f:
            json.dump(a,f)