import base64
encoded = base64.b64encode(open("N:\Work\personal\/blue-pi-interview\/backend\img/a.png", "rb").read()).decode("utf-8")
print(encoded)