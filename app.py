import streamlit as st

from services.maps_api import get_coordinates, search_places
from analysis.score import calcular_score
from components.map_view import render_map


st.set_page_config(page_title="Business Location Analyzer")

st.title("📍 Plataforma de Inteligência Comercial")

st.write(
    "Analise o potencial de uma região para abertura de um negócio."
)


TIPOS_NEGOCIO = {
    "Cafeteria": "cafe",
    "Restaurante": "restaurant",
    "Academia": "gym",
    "Farmácia": "pharmacy",
    "Padaria": "bakery"
}


local = st.text_input(
    "Digite a localização",
    placeholder="Ex: Vila Mariana, São Paulo"
)


negocio = st.selectbox(
    "Selecione o tipo de comércio",
    list(TIPOS_NEGOCIO.keys())
)


raio = st.slider(
    "Raio de análise (metros)",
    min_value=500,
    max_value=5000,
    value=1000,
    step=100
)


if st.button("Analisar região"):

    if not local:
        st.warning("Digite uma localização")

    else:
        with st.spinner("Analisando região..."):

            coords = get_coordinates(local)
            if coords is None:
                st.error("Não foi possível encontrar a localização")

            else:

                lat, lng = coords
                

                lugares = search_places(
                    lat,
                    lng,
                    TIPOS_NEGOCIO[negocio],
                    raio
                )
                if not lugares:
                    st.warning(
                        "Nenhum estabelecimento foi encontrado nessa região para o tipo de comércio selecionado."
                        
                    )
                    render_map(lat, lng, lugares)
                else:
                    resultado = calcular_score(lugares)
                    st.subheader("📊 Resultado da análise")
                    
                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Score da região",
                            resultado["score"]
                        )

                        st.metric(
                            "Concorrentes",
                            resultado["concorrentes"]
                        )

                    with col2:
                        st.metric(
                            "Rating médio",
                            resultado["rating_medio"]
                        )

                        st.metric(
                            "Reviews médio",
                            resultado["reviews_medio"]
                        )
                    if resultado["score"] >= 80:
                        st.success("Excelente região para o negócio")

                    elif resultado["score"] >= 60:
                        st.warning("Região com potencial moderado")

                    else:
                        st.error("Região com baixo potencial")
                    render_map(lat, lng, lugares)