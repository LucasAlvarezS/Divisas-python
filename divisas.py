import requests

url = "https://api.exchangeratesapi.io/v1/latest?access_key=43479b594d119ce4e4bd3a0c41359fb0&format=1"

base = input ("Ingresa tú divisa local: ")
cant = float(input("Cantidad: "))
div = input("Divisa: ")

try:
    resp = requests.get(url + base)
    data = resp.json()
    divisas = data["rates"]
except:
    print("Ha habido un error")
    raise

if div.upper() in divisas.keys():
    result = divisas[div.upper()] * cant
    format_result = "{:,.2f}".format(result)
    print(f"Resultado: {format_result}")