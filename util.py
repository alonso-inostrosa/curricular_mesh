import json

def load_data(filename):
    with open(filename, 'r') as myjsonfile:
        data=myjsonfile.read()
    jsondata = json.loads(data)
    return jsondata