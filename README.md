
# 🧠 Cyber Intelligence Dashboard

Una herramienta web local construida para monitorear ataques de ransomware en tiempo real, ayudando a analistas y equipos de ciberseguridad a detectar patrones clave, filtrar eventos y visualizar amenazas por país, grupo y actividad.

---

## 📌 Tabla de Contenidos

- [🔍 Descripción](#-descripción)
- [⚙️ Tecnologías](#️-tecnologías)
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [🚀 Cómo ejecutar localmente](#-cómo-ejecutar-localmente)
- [📊 Funcionalidades](#-funcionalidades)
- [🧪 Capturas](#-capturas)
- [📎 Notas](#-notas)

---

## 🔍 Descripción

Este dashboard consume la API pública de [https://ransomware.live](https://ransomware.live) y permite:

- Ver víctimas recientes de ransomware
- Filtrar por país, grupo, actividad y fechas
- Visualizar gráficos Pareto por:
  - País
  - Grupo de ataque
  - Actividad afectada

Todo se ejecuta localmente sin necesidad de despliegue.

---

## ⚙️ Tecnologías

- Python 3
- Flask
- Jinja2
- Chart.js
- HTML + CSS (con diseño responsive)
- JavaScript (dashboardCharts.js)
- API pública: `https://api.ransomware.live/v2`

---

## 📂 Estructura del Proyecto
.
- ├── app.py # Archivo principal Flask
- ├── victims.py # Funciones para consultar y procesar víctimas
- ├── dashboard.py # Funciones para agrupar datos del dashboard
- ├── utils.py # Funciones auxiliares
- ├── templates/  
  - │ ├── base.html # Plantilla base con menú y estilos
  - │ ├── victims.html # Página de tabla de víctimas con filtros
  - │ └── dashboard.html # Página con visualizaciones
- ├── static/
  - | └── images/
    - |   └── logo.png # Logo usado en el banner
  - │ └── js/
    - │   └── dashboardCharts.js # Script para generar los gráficos Pareto
- ├── README.md # Este archivo
- └── requirements.txt # dependencias del entorno virtual
- └── .gitignore # Elementos a ignorar

## 🚀 Cómo ejecutar localmente
- 1. Clonar el repositorio
  -    bash
    -        git clone https://github.com/tu_usuario/cyber-intel-dashboard.git
    -        cd cyber-intel-dashboard
- 2. Crear entorno virtual (opcional pero recomendado)
  -    bash
    -        python -m venv venv
    -        source venv/bin/activate  # Linux/Mac
    -        venv\Scripts\activate     # Windows
- 3. Instalar dependencias
  -    bash
    -        pip install flask requests
- 4. Ejecutar la app
  -    bash
    -        python app.py
    -        Abre tu navegador en http://127.0.0.1:5000

## 📊 Funcionalidades
### Página de Víctimas (/recentVictims)
- Tabla ordenada de víctimas recientes
- Filtros por país, grupo, actividad
- Filtro por rango de fechas
-Enlace a detalles del ataque

### Página de Dashboard (/dashboard)
- Filtros aplicables al dashboard
- Pareto de ataques por país
- Pareto de ataques por grupo
- Pareto de ataques por actividad

## 🧪 Capturas

## 📎 Notas
- El proyecto está diseñado para funcionar localmente, no requiere despliegue.
- La API es pública y puede cambiar su estructura. Se recomienda validar el endpoint si no carga correctamente.
- El diseño está optimizado para escritorio y dispositivos móviles.
