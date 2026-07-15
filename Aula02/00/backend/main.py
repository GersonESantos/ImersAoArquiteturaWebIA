from fastapi import FastAPI

# Inicializa a aplicação FastAPI
app = FastAPI()

# Definição do endpoint raiz (GET "/")
# O decorador @app.get("/") mapeia requisições HTTP GET na raiz da URL para esta função.
@app.get("/")
def hello_world():
    # Retorna o JSON com a mensagem solicitada
    return {"mensagem": "Olá, mundo! 🌍"}
