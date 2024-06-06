from flask import Flask, render_template
from evento import Evento
from organizacao import Organizacao
from sala import Sala
from servicos import Servico
from transporte import Transporte

app = Flask(__name__)

sala1 = Sala(1, "Laboratório de informática 1000", "Bloco 1", "_img/lab1.jpg")
sala2 = Sala(2, "Biblioteca","Bloco 2", "_img/biblioteca.jpg")
sala3 = Sala(3, "Auditório", "Bloco 3", "_img/auditorio.jpg")
sala4 = Sala(4, "Laboratório de informática 1001", "Bloco 1", "_img/lab2.jpg")
sala5 = Sala(5, "Lanchonete", "Pátio Principal", "_img/lanchonete.jpg")
sala6 = Sala(6, "Estacionamento", "Pátio Principal", "_img/estacionamento.jpg")
sala7 = Sala(7, "Enfermaria", "Bloco 2", "_img/enfermaria.jpg")

palestra = Evento(1, "Palestra IA", 
                        "Palestra",
                        "Prof. Roberto",
                        "Vivemos em uma era onde a tecnologia avança a passos largos, e a Inteligência Artificial (IA) está na vanguarda dessa revolução.",
                        "21/05/2024",
                        "19:00",
                        [sala3.nome],
                        "_img/ia.jpg")
workshop = Evento(2, "Workshop Programação Front-End", 
                        "Workshop",
                        "Prof. Roberto",
                        "Workshop para introdução à programação front-end para desenvolvimento de aplicações Web para o dia a dia.",
                        "22/05/2024",
                        "19:00",
                        [sala1.nome],
                        "_img/front-end.jpg")

linha1 = Transporte(1, "Escolar Prefeitura", ["18:00","22:00"], "Cidade Vizinha x Campus")
linha2 = Transporte(1, "Escolar Prefeitura", ["17:00","22:00"], "Cidade Vizinha 2 x Campus")
linha3 = Transporte(1, "Escolar Prefeitura", ["18:30","22:10"], "Cidade Vizinha 3 x Campus")

org1 = Organizacao(1, "Clube de robótica", 
                   "Clube", 
                   "O Clube de Robótica é dedicado à construção e programação de robôs. Os membros participam de competições regionais e nacionais, aprendendo sobre engenharia, eletrônica e programação.", 
                   "Clube de Robótica Ganha Primeira Competição Nacional", 
                   ["Competição de Robótica Intercampus", 
                    "15/06/2024",[sala1.nome]],
                    "_img/robot.png")
org2 = Organizacao(2, "Associação de estudantes internacionais",
                   "Associação",
                   "A Associação de Estudantes Internacionais oferece suporte e promove a integração dos alunos estrangeiros no campus.",
                   "Semana Cultural Internacional Atrai Centenas de Participantes",
                   ["Festa Internacional de Boas-Vindas", "22/08/2024", [sala6.nome]],
                   "_img/connections.png")

servico1 = Servico(1, "Centro de atendimento de saúde", "oferece atendimento médico e psicológico aos estudantes.", [sala7.nome], ["09:00", "22:00"])
servico2 = Servico(2, "Biblioteca Central", "A Biblioteca Central oferece um vasto acervo de livros, periódicos e recursos digitais.", [sala2.nome], ["09:00","22:00"])

evento_all = [palestra, workshop]
campus_all = [sala1, sala2, sala3, sala4, sala5, sala6, sala7]
servico_all = [servico1, servico2]
linha_all = [linha1, linha2, linha3]
org_all = [org1, org2]

@app.route('/')
def index():
    return render_template("index.html", evento_list = evento_all, org_list = org_all)

@app.route('/campus-info')
def campusList():
    return render_template("campus-info.html", campus_list = campus_all)

@app.route('/transporte')
def transporte():
    return render_template("transporte.html", transporte = linha_all)

@app.route('/servico')
def servico():
    return render_template("servicos.html", servico = servico_all)

@app.route('/orgInfo/<int:id>')
def orgInfo(id:int):
    for orgInfo in org_all:
        if orgInfo.id == id:
            return render_template("org-info.html", orgInfo = orgInfo)
    return "<h1>Página não encontrada</h1>"

@app.route('/eventoInfo/<int:id>')
def eventoInfo(id:int):
    for eventoInfo in evento_all:
        if eventoInfo.id == id:
            return render_template("evento-info.html", eventoInfo = eventoInfo)
    return "<h1>Página não encontrada</h1>"

@app.route('/infraInfo/<int:id>')
def campusInfo(id:int):
    for campusInfo in campus_all:
        if campusInfo.id == id:
            return render_template("infra-info.html", campusInfo = campusInfo)
    return "<h1>Página não encontrada</h1>"