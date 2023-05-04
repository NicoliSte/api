from typing import Optional
from fastapi import FastAPI
import pytz
from datetime import datetime

app = FastAPI()

@app.get("/timezone")
async def get_time(timezone: Optional[str] = None):
    """
    Endpoint que retorna a data e hora atual para um determinado fuso horário.

    Args:
        timezone (str): O nome do fuso horário desejado. Se não for fornecido, o fuso horário UTC será usado.

    Returns:
        dict: Um dicionário contendo a data e hora atual para o fuso horário fornecido.
    """
    # Se o fuso horário não for fornecido, use o UTC.
    if not timezone:
        timezone = "UTC"

    # Verifique se o fuso horário fornecido é válido.
    if timezone not in pytz.all_timezones:
        return {"error": "Fuso horário inválido."}

    # Obtenha o objeto timezone correspondente ao fuso horário fornecido.
    tz = pytz.timezone(timezone)

    # Obtenha a data e hora atuais para o fuso horário fornecido.
    current_time = datetime.now(tz)

    # Crie um dicionário com a data e hora atuais formatadas como strings.
    result = {
        "timezone": timezone,
        "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    }

    return result
