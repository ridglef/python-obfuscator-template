import base64

def transform(src: str):
    return "exec(__import__('base64').b64decode(\"" + base64.b64encode(src.encode()).decode() + "\"))"
