# FastAPI Timezone

Endpoint que retorna a data e hora atual para um determinado fuso horário.

## Requisitos

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [pytz](https://pypi.org/project/pytz/)

## Dependências

As seguintes dependências são necessárias para executar a API:

- `fastapi`: para criação do aplicativo web
- `pytz`: para trabalhar com fusos horários
- `datetime`: para trabalhar com datas e horas

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/NicoliSte/api.git
   ```

2. Crie e ative um ambiente virtual (opcional):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Inicie a aplicação:

   ```bash
   python -m uvicorn main:app --reload
   ```

2. Acesse o endpoint em um navegador ou com o comando `curl`, por exempo:

   ```
   http://localhost:8000/timezone?timezone=America/Sao_Paulo 
   http://localhost:8000/timezone?timezone=America/New_York
   ```

   O parâmetro `timezone` é opcional. Se não for fornecido, a hora UTC será retornada.

## Exemplo de resposta

```json
{
  "timezone": "America/Sao_Paulo",
  "current_time": "2023-05-04 17:50:00 -03"
}
```

## Autor 

Nicoli Stefani
