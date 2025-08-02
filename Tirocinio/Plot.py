import geopandas as gp
import plotly.express as px

gdf = gp.read_file("PuntiCampionatoriFinali.gpkg")
gdf = gdf.dropna(subset=["Altitudine1", "value"])

# Crea colonna stringa coordinate per tooltip (opzionale)
gdf["coords"] = gdf.geometry.apply(lambda point: f"({point.x:.3f}, {point.y:.3f})")

fig = px.scatter(
    gdf,
    x="Altitudine1",
    y="value",
    title="Grafico Interattivo Altitudine vs Value",
    labels={"Altitudine1": "Altitudine (m)", "value": "Valore"},
    hover_data=["Altitudine1", "value", "coords"],  # escludo geometry!
    color="value",
    size="value",
    size_max=15,
    template="plotly_white"
)

fig.write_html("grafico_altitudine_value.html", auto_open=True)
