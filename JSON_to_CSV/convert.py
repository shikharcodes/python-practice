import json

if __name__ == "__main__":
    try:
        with open("inputdata.json", "r") as rf:
            data = json.loads(rf.read())
        output = ",".join([*data[0]])
        for d in data:
            output += f"\n{d['Name']},{d['Age']},{d['BirthYear']}"
        with open("outputdata.csv", "w") as wf:
            wf.write(output)
    except Exception as e:
        print(f"Error: {str(e)}")