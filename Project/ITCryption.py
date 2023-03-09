import base64
import json

def b64encode(string):
    string_bytes = string.encode("utf-8")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("utf-8")
    return base64_string

def b64decode(b64):
    base64_bytes = b64.encode("utf-8")
    string_bytes = base64.b64decode(base64_bytes)
    string = string_bytes.decode("utf-8")
    return string

def encode(data):
    # jsonData = json.dumps(data).encode("utf-8")
    jsonData = json.dumps(data)
    b64CharsArray = []
    for char in jsonData:
        b64CharsArray.append(b64encode(char))
    charsSTR = b64encode("|".join(b64CharsArray))
    
    return b64encode(charsSTR)

def decode(data):
    charsSTR = b64decode(data)
    charsBase64Array = charsSTR.split("|")
    strData = ""
    for char in charsBase64Array:
        strData += b64decode(char)

    s = ""
    for char in strData.split("|"):
        s += b64decode(char).encode("utf-8").decode("utf-8")

    return json.loads(s)