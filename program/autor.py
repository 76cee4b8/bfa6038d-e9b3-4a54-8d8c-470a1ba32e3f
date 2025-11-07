class Autor:

    def __init__(self, nome):
        
        self.nome = nome

    def __del__(self):

        print(f"O autor {self.nome} foi removido.")