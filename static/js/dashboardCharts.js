// Cargo un grafico de pareto (barras + línea de % acumulado) en un canvas de Chart.js
function loadParetoChart(canvasId, labels, values, cumulative, label) {
    // Obtengo el <canvas> por ID y si no lo encuentra se cancela
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    //Crep la grafica con grafico principal como barras y secundario como linea
    new Chart(ctx, {
        type: "bar",
        //Configuro la data del grafico como los valores que va a tener y los labels de los ejes
        data: {
            labels: labels,
            datasets: [
                //Asigno los valores para las barras
                {
                    label: label,
                    data: values,
                    backgroundColor: "rgba(75, 192, 192, 0.6)",
                    yAxisID: 'y'
                },
                //Asigno los valores para las lineas
                {
                    label: "Cumulative %",
                    data: cumulative,
                    type: "line",
                    borderColor: "rgba(255, 99, 132, 1)",
                    yAxisID: 'y1'
                }
            ]
        },
        //Le pongo la posibilidad de que al pasar el mouse sobre la grafica me de info,
        //de que sea responsive, y le pongo titulo dinamico a la grafica
        options: {
            responsive: true,
            interaction: {
                mode: 'index',
                intersect: false
            },
            stacked: false,
            plugins: {
                title: {
                    display: true,
                    text: label + ' (Pareto)'
                }
            },
            scales: {
                //Configuro los ejes Y de mi grafica
                y: {
                    type: 'linear',
                    position: 'left',
                    title: { display: true, text: 'Quantity' }
                },
                y1: {
                    type: 'linear',
                    position: 'right',
                    title: { display: true, text: 'Cumulative %' },
                    grid: { drawOnChartArea: false },
                    min: 0,
                    max: 100,
                    ticks: { callback: value => value + '%' }
                }
            }
        }
    });
}

//Creo una función para leer el JSON embebido en el script de tipo application/json y lo parseo
function parseJSONFromScript(id) {
    const raw = document.getElementById(id)?.textContent;
    if (!raw) return null;
    try {
        return JSON.parse(raw);
    } catch (e) {
        console.error(`Error parsing JSON from #${id}:`, e);
        return null;
    }
}

//Creo una función para convertir los datos de mis objetos en datos ordenados para mis gráficos de Pareto
function prepareParetoData(dataObj) {
    //Establezco el orden descendente y ordeno los datos
    const entries = Object.entries(dataObj).sort((a, b) => b[1] - a[1]);
    const labels = entries.map(entry => entry[0]);
    const values = entries.map(entry => entry[1]);

    //Creo un elemento acumulativo que me capta los valores porcentuales de los ataques 
    //dependiendo de la categoria (Pais, actividad, grupo)
    const total = values.reduce((sum, val) => sum + val, 0);
    const cumulative = [];
    let cumulativeSum = 0;

    for (let val of values) {
        cumulativeSum += val;
        cumulative.push((cumulativeSum / total * 100).toFixed(2));
    }

    return { labels, values, cumulative };
}

//Espro a que el DOM cargue y los datos esten disponibles para poder generar los graficos pareto 
window.addEventListener('DOMContentLoaded', () => {
    //Establezco cuales graficos voy a hacer
    const datasets = [
        { id: 'country-data', canvas: 'paretoChartCountry', label: 'Attacks by country' },
        { id: 'group-data', canvas: 'paretoChartGroup', label: 'Attacks by group' },
        { id: 'activity-data', canvas: 'paretoChartActivity', label: 'Attacks by activity' }
    ];


    datasets.forEach(set => {
        //Obtengo la información y la parseo a un JSON
        const rawData = parseJSONFromScript(set.id);
        if (rawData) {
            //Organizo mi información en el formato requerido y genero el grafico pareto
            const pareto = prepareParetoData(
                Object.fromEntries(rawData.labels.map((l, i) => [l, rawData.data[i]]))
            );
            loadParetoChart(set.canvas, pareto.labels, pareto.values, pareto.cumulative, set.label);
        }
    });
});
