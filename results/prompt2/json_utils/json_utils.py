import json

def read_json(fpath):
  with open(fpath, 'r') as f:
    obj = json.load(f)
  return obj

def write_json(path,data):
    with open(path, "w") as file:
        json.dump(data, file,indent = 4)
    file.close()