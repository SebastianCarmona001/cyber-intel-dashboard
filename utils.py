#Importo las librerías necesarias
from datetime import datetime

#Creo una función para normalizar la fecha a "dd/mm/YYYY HH:MM"
def parse_date(date_str):

    #Si el valor es none o vacio devuelvo "N/A"
    if not date_str:
        return "N/A"
    #Establezco la lista de posibles formatos a normalizar
    formatos = [
        "%Y-%m-%d %H:%M:%S.%f",  
        "%Y-%m-%d %H:%M:%S",     
        "%d/%m/%Y %H:%M",        
        "%d/%m/%Y",              
        "%Y-%m-%d"               
    ]

    #Itero sobre los formatos y lo comparo con el valor que me entrega 
    #y lo convierto al formato que yo quiero, si no se asocia a ninguno 
    #de mis formatos me devuelve "N/A"
    for fmt in formatos:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%d/%m/%Y %H:%M")
        except ValueError:
            continue
    return "N/A"
