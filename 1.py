import base64
import json

with open("keys.json") as f:
    data = json.load(f)
    datstr = json.dumps(data)
    encode = base64.b64encode(datstr.encode("utf-8"))
    print(base64.b64decode(encode))


    