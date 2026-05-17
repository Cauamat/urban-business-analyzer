import folium
from streamlit_folium import st_folium


def render_map(lat, lng, lugares):

    mapa = folium.Map(
        location=[lat, lng],
        zoom_start=14
    )

    folium.Marker(
        [lat, lng],
        tooltip="Local analisado",
        icon=folium.Icon(color="red")
    ).add_to(mapa)

    for lugar in lugares:

        folium.Marker(
            [lugar["lat"], lugar["lng"]],
            popup=lugar["nome"]
        ).add_to(mapa)

    st_folium(
        mapa,
        width=700,
        height=500,
        returned_objects=[]
    )