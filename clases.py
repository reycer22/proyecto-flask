class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña


class Anuncio:
    def __init__(self, id, titulo, clicks=0):
        self.id = id
        self.titulo = titulo
        self.clicks = clicks

    def registrar_click(self):
        self.clicks += 1
        print(f"El anuncio '{self.titulo}' ahora tiene {self.clicks} clic(s).")

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.anuncios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_anuncio(self, anuncio):
        self.anuncios.append(anuncio)
