from flask import Flask, render_template
from evento import Evento
from organizacao import Organizacao
from palestrante import Palestrante
from sala import Sala
from servicos import Servico
from transporte import Transporte

app = Flask(__name__)

roberto = Palestrante(1, "Roberto Jr", "Estudante")
eventoTeste = Evento(1, "Evento Teste", 
                        "Palestra",
                        "Roberto",
                        "Este é um belo evento",
                        "21/05/2024",
                        "19:00",
                        "Auditório")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/eventoInfo')
def eventoInfo():
    return render_template("evento-info.html")