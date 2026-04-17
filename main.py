#Fastapi
# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#Para salvar o css em outra pasta 
from fastapi.staticfiles import StaticFiles

# Rodar o sevidor: python -m uvicorn main:app --reload
app = FastAPI(title="Gestão escolar")


#Configurar o diretório dos html 
templates = Jinja2Templates(directory="templates")

#Mapeia a pasta static para servir arquivos (CSS, IMG, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

#Abrir/retomar html:
# Rota - endpoint
# Método HTTP - GET, POST, PUT, DELETE
# GET = Pegar/listar/Exibir
# Post = Criar/adicionar
# PUT = Atualizar 
# DELETE = Deletar
@app.get("/")
def pagina_inicial(request: Request):
    return templates.TemplateResponse(
        request,
        "pagina_inicial.html",
        {"request": request}
    )

@app.get("/alunos")
def listar_alunos(request: Request):
    alunos = [
        {"nome": "Miguelzinho", "nota": 5},
        {"nome": "Felipinho", "nota": 7},
        {"nome": "Yago", "nota": 8},
        {"nome": "Messi", "nota": 10},
    ]
    return templates.TemplateResponse(
        request,
        "alunos.html",
        {"request": request, "alunos": alunos}
    )
