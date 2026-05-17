import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

if GOOGLE_MAPS_API_KEY is None:
    raise ValueError("API KEY não encontrada no arquivo .env")