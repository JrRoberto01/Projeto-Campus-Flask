class Evento:
    def __init__(self, id, nome, tipo, palestrante, descricao, data, horario, local, url_foto) -> None:
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.palestrante = palestrante
        self.descricao = descricao
        self.data = data
        self.horario = horario
        self.local = local
        self.url_foto = url_foto