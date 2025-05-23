#Importo request para poder hacer peticiones de HTTP a la API
import requests

#Creo una variable con el valor generico de la URL de mi API
BASE_URL = 'https://api.ransomware.live/v2'

#Defino una función que me trae la información de las victimas
#y los valores de los filtros
def get_recent_victims():
    try:
        #Extiendo la URL para hacer la petición adecuada y realizo el GET
        url = f"{BASE_URL}/recentvictims"
        response = requests.get(url)

        #Pido el status de la petición para que salte si es != 200
        response.raise_for_status()

        #Convierto la data a un diccionario de python
        data = response.json()

        #Creo una lista a la que le voy a asignar la info que traiga de la API
        victims = []

        #Itero sobre la data y le voy agregando filas a mi lista con la info que considero util
        for item in data:
            victims.append({
                "victim": item.get("victim", "N/A"),
                "group": item.get("group", "N/A"),
                "activity": item.get("activity", "N/A"),
                "discovered": item.get("discovered", "N/A"),
                "attackdate": item.get("attackdate", "N/A"),
                "country": item.get("country", "N/A"),
                "url": item.get("url", "#")
            })

        return victims

    #Si tengo algun error lo muestro en consola
    except requests.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return []

#Cuento cuantas victimas hay por pais iterando sobre las victimas
def count_attacks_by_country(victims):
    counts = {}
    for v in victims:
        country = v.get("country")
        if country:
            counts[country] = counts.get(country, 0) + 1
    return counts

#Cuento cuantas victimas hay por grupo iterando sobre las victimas
def count_attacks_by_group(victims):
    counts = {}
    for v in victims:
        group = v.get("group")
        if group:
            counts[group] = counts.get(group, 0) + 1
    return counts

#Cuento cuantas victimas hay por actividad iterando sobre las victimas
def count_attacks_by_activity(victims):
    counts = {}
    for v in victims:
        activity = v.get("activity")
        if activity:
            counts[activity] = counts.get(activity, 0) + 1
    return counts