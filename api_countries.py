import requests


def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"Nombre Oficial en Español : {pais['translations']['spa']['official']}")
        print(f"La Capital es : {pais['capital'][0]}")
        print(f"Código de teléfono: {pais['idd']['root'] + pais['idd']['suffixes'][0]}")

        if "currencies" in pais:
            for codigo_moneda, info_moneda in pais["currencies"].items():
                nombre_moneda = info_moneda["name"]
                print(f"Tipo de moneda ({codigo_moneda}): {nombre_moneda}")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,idd,currencies'
listar_nombre_paises(url)
