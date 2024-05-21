class Organizacao:
    def __init__(self, id, tipo ,nome, descricao, noticias, eventos) -> None:
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.noticias = noticias
        self.eventos = eventos