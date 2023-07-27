import requests

def get_countries():
  """Obtiene una lista de todos los países de la API restcountries.com."""
  response = requests.get("https://restcountries.com/v3.1/all")
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception("Error getting countries from restcountries.com API")

def get_pais_con_mayor_poblacion():
  """Obtiene el país con la población más grande."""
  countries = get_countries()
  largest_population = 0
  largest_country_common_name = None
  for country in countries:
    if country["population"] > largest_population:
      largest_population = country["population"]
      largest_country_common_name = country["name"]["common"]
  return largest_country_common_name

def get_pais_con_mayor_area():
  """Obtiene el país con el área más grande ."""
  countries = get_countries()
  largest_area = 0
  largest_country_info = None
  for country in countries:
    if country["area"] > largest_area:
      largest_area = country["area"]
      largest_country_info = {
        "official_name": country["name"]["official"],
        "area": country["area"]
      }
  return largest_country_info

def get_poblacion_total():
  """Obtiene la población total de todos los países."""
  countries = get_countries()
  total_population = 0
  for country in countries:
    total_population += country["population"]
  return total_population

def get_media_poblacion():
  """Obtiene la media de población de todos los países."""
  countries = get_countries()
  total_population = 0
  for country in countries:
    total_population += country["population"]
  media_population = total_population / len(countries)
  return media_population

def get_mediana_poblacion():
  """Obtiene la mediana de población de todos los países."""
  countries = get_countries()  # Suponiendo que obtener_paises() devuelve una lista de diccionarios con la información de los países
  population_values = [pais["population"] for pais in countries]
  population_values.sort()
  n = len(population_values)
  if n % 2 == 0:
    mediana_population = (population_values[n // 2 - 1] + population_values[n // 2]) / 2
  else:
    mediana_population = population_values[n // 2]
  return mediana_population

def get_moda_poblacion():
  """Obtiene la moda de población de todos los países."""
  countries = get_countries()
  populations = []
  for country in countries:
    populations.append(country["population"])
  moda_population = max(set(populations), key=populations.count)
  return moda_population

if __name__ == "__main__":
  print("País con mayor población:", get_pais_con_mayor_poblacion())
  print("País con mayor área:", get_pais_con_mayor_area())
  print("Población total:", get_poblacion_total())
  print("Media de población:", get_media_poblacion())
  print("Mediana de población:", get_mediana_poblacion())
  print("Moda de población:", get_moda_poblacion())
