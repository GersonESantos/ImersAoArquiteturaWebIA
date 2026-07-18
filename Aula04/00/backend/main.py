import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Inicializa a aplicação FastAPI
app = FastAPI()

# Definição do caminho absoluto da pasta de imagens.
# Isso garante que a pasta correta será encontrada independentemente de onde o script seja executado.
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configuração dos arquivos estáticos:
# "Monta" a pasta de imagens na rota "/imgs".
# Com isso, um arquivo em "figurinhas/01-alan-turing.jpg" pode ser acessado na URL "/imgs/01-alan-turing.jpg".
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Definição do endpoint para listar figurinhas (GET "/figurinhas")
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna uma lista contendo as duas figurinhas de exemplo solicitadas,
    # agora incluindo o campo imagem_url que usa o caminho estático configurado acima.
    return [
        {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/imgs/01-alan-turing.jpg"},
        {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/imgs/02-john-mccarthy.jpg"}
    ]
