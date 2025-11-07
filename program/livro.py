class Livro:

    def __init__(self, isbn, nome, autor):
        
        self.isbn  = isbn
        self.nome  = nome
        self.autor = autor

    def __eq__(self, isbn):
        
        return self.isbn == isbn
    
    def exportar(self, caminho):

        with open(caminho + '/' + self.nome + '.txt', 'w') as file:
            
            file.write(f'{self.nome} - {self.autor.nome}')