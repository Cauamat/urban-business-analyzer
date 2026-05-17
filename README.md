# 📍 Urban Business Analyzer

Uma plataforma inteligente desenvolvida em Python capaz de analisar o potencial comercial de uma região utilizando dados da API do Google Maps. O sistema permite que o usuário informe um tipo de comércio e uma localização específica para receber uma pontuação baseada na concorrência, avaliações e movimentação comercial da região.

---

# 🚀 Objetivo do Projeto

O projeto tem como objetivo auxiliar empreendedores na escolha de locais estratégicos para abertura de novos negócios, reduzindo riscos e tornando a tomada de decisão mais orientada por dados.

---

# 🧠 Funcionalidades

* Busca de localização por endereço
* Conversão de endereço em coordenadas geográficas
* Busca de estabelecimentos próximos
* Cálculo de score da região
* Exibição de métricas comerciais
* Mapa interativo com concorrentes
* Interface web utilizando Streamlit
* Integração com Google Maps API

---

# 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Requests
* Folium
* Streamlit-Folium
* Google Maps API
* Python Dotenv

---

# 📂 Estrutura do Projeto

```bash
urban-business-analyzer/

├── app.py
├── config.py
├── requirements.txt
├── .env

├── services/
│   └── maps_api.py

├── analysis/
│   └── score.py

├── components/
│   └── map_view.py
```

---

# ⚙️ Configuração do Projeto

## 1. Clone o repositório

```bash
git clone <url-do-repositorio>
```

---

## 2. Acesse a pasta

```bash
cd urban-business-analyzer
```

---

## 3. Crie o ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_MAPS_API_KEY=SUA_CHAVE_AQUI
```

É necessário possuir uma chave válida da plataforma Google Maps com as APIs:

* Geocoding API
* Places API

habilitadas no Google Cloud.

---

# ▶️ Como Executar

```bash
streamlit run app.py
```

---

# 📊 Como Funciona o Score

O sistema calcula uma pontuação baseada em:

* Quantidade de concorrentes
* Avaliação média dos estabelecimentos
* Quantidade média de avaliações
* Popularidade comercial da região

A pontuação varia de:

* 0 → Baixo potencial
* 100 → Alto potencial

---

# 🗺️ Funcionalidades Futuras

* Histórico de pesquisas
* Banco de dados SQLite
* Comparação entre regiões
* Dashboard analítico
* Machine Learning
* Heatmap comercial
* Deploy em nuvem

---

# 📸 Exemplo de Uso

1. Digite uma localização
2. Escolha um tipo de comércio
3. Defina o raio de análise
4. Clique em “Analisar Região”
5. Visualize o score, concorrentes e mapa interativo

---

# 👨‍💻 Autor

Projeto desenvolvido por estudantes da universidade virtual do estado de São Paulo para disciplina de projeto integrador 5 
