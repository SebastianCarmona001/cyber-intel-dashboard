# Se importan todas las librerias y archivos relacionados
from flask import Flask, render_template, request
from victims import get_recent_victims, count_attacks_by_group, count_attacks_by_country, count_attacks_by_activity
from datetime import datetime

# Inicio la aplicación de flask
app = Flask(__name__)

@app.route('/recentVictims')
def recent_victims():
    # Capturo los datos de los filtros que uso desde la URL por medio de request.args.get
    country_filter = request.args.get('country')
    group_filter = request.args.get('group')
    activity_filter = request.args.get('activity')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    #Llamo la funcion que esta en victims.py para traer la data de la API
    victims = get_recent_victims()

    # Aplico los filtros de país, grupo y actividad
    if country_filter:
        victims = [v for v in victims if v["country"] and v["country"].lower() == country_filter.lower()]
    if group_filter:
        victims = [v for v in victims if v["group"] and v["group"].lower() == group_filter.lower()]
    if activity_filter:
        victims = [v for v in victims if v["activity"] and v["activity"].lower() == activity_filter.lower()]

    #Aplico los filtros de rango de fecha de ataque
    if start_date or end_date:
        def in_range(victim):
            try:
                attack_date = datetime.fromisoformat(victim["attackdate"])
            except Exception:
                return False
            if start_date and attack_date < datetime.fromisoformat(start_date):
                return False
            if end_date and attack_date > datetime.fromisoformat(end_date):
                return False
            return True
        victims = [v for v in victims if in_range(v)]

    # Creo las opciones de los filtros ya que estos van a ser selects con opciones unicas, por eso el set
    countries = sorted(set(v["country"] for v in victims if v["country"]))
    groups = sorted(set(v["group"] for v in victims if v["group"]))
    activities = sorted(set(v["activity"] for v in victims if v["activity"]))

    #Renderizo la plantilla de HTML llamada victims.html con los datos filtrados y con los valores de los filtros
    return render_template('victims.html',
                           victims=victims,
                           countries=countries,
                           groups=groups,
                           activities=activities,
                           selected_country=country_filter,
                           selected_group=group_filter,
                           selected_activity=activity_filter,
                           start_date=start_date,
                           end_date=end_date)

@app.route('/dashboard')
def dashboard():

    # Capturo los datos de los filtros que uso desde la URL por medio de request.args.get
    country_filter = request.args.get('country')
    group_filter = request.args.get('group')
    activity_filter = request.args.get('activity')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    #Llamo la funcion que esta en victims.py para traer la data de la API
    victims = get_recent_victims()

    # Aplico los filtros de país, grupo y actividad
    if country_filter:
        victims = [v for v in victims if v["country"] and v["country"].lower() == country_filter.lower()]
    if group_filter:
        victims = [v for v in victims if v["group"] and v["group"].lower() == group_filter.lower()]
    if activity_filter:
        victims = [v for v in victims if v["activity"] and v["activity"].lower() == activity_filter.lower()]

    #Aplico los filtros de rango de fecha de ataque
    if start_date or end_date:
        def in_range(victim):
            try:
                attack_date = datetime.fromisoformat(victim["attackdate"])
            except Exception:
                return False
            if start_date and attack_date < datetime.fromisoformat(start_date):
                return False
            if end_date and attack_date > datetime.fromisoformat(end_date):
                return False
            return True
        victims = [v for v in victims if in_range(v)]

    # Calculo en victims.py los valores necesarios para realizar los graficos
    total_attacks = len(victims)
    attacks_by_group = count_attacks_by_group(victims)
    attacks_by_country = count_attacks_by_country(victims)
    attacks_by_activity = count_attacks_by_activity(victims)

    # Creo las opciones de los filtros ya que estos van a ser selects con opciones unicas, por eso el set
    countries = sorted(set(v["country"] for v in victims if v["country"]))
    groups = sorted(set(v["group"] for v in victims if v["group"]))
    activities = sorted(set(v["activity"] for v in victims if v["activity"]))

    #Renderizo la plantilla de HTML llamada dashboard.html con los datos filtrados, con los valores de los filtros
    #y con las agrupaciones que hice para los graficos
    
    return render_template('dashboard.html',
                           total_attacks=total_attacks,
                           attacks_by_group=attacks_by_group,
                           attacks_by_country=attacks_by_country,
                           attacks_by_activity=attacks_by_activity,
                           countries=countries,
                           groups=groups,
                           activities=activities,
                           selected_country=country_filter,
                           selected_group=group_filter,
                           selected_activity=activity_filter,
                           start_date=start_date,
                           end_date=end_date)


# Arranco la aplicación
if __name__ == "__main__":
    app.run(debug=True)