class Evento:
    def __init__(self, id, nome, tipo, palestrante, descricao, data, horario, local) -> None:
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.palestrante = palestrante
        self.descricao = descricao
        self.data = data
        self.horario = horario
        self.local = local