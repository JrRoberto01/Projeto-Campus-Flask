class Organizacao:
    def __init__(self, id, nome, tipo, descricao, noticias, eventos, url_foto) -> None:
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.noticias = noticias
        self.eventos = eventos
        self.url_foto = url_foto