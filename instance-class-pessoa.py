class Pessoa:
    def __init__ (self, nome, cidade, telefone, email):
        self.nome=nome
        self.cidade=cidade
        self.telefone=telefone
        self.email=email
    
    #criando métodos
    def falar(self):
        print("Olá, meu nome é "+self.nome+" e sou da cidade de "+self.cidade)
    
    #criando o segundo método
    def ler_livro(self):
        print("Às vezes sou feliz na minha ternura,às vezes me engano, o que é mais comum.")
#instanciando...
pessoa1= Pessoa("Mary", "São Carlos", 16981345678, "mary01@gmail.com")
#Verificando se o objeto pessoa possuí o atributo nome
hasattr(pessoa1,"nome")
#
pessoa1.ler_livro()
pessoa1.falar()