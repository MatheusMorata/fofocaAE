import os

# Cria uma identidade dentro da rede
def criar_identidade(nome):
    comando = "freechains keys shared '" + nome + "'"
    os.system(comando)

# Posta um texto dentro da rede
def post(texto,chave):
    comando1 = "freechains chains join '$UERJ' " + chave 
    comando2 = "freechains chain '$UERJ' post inline '" + texto + "'"
    os.system(comando1)
    os.system(comando2)

def consult_msgs():
    comando1 = "freechains chain '$UERJ' consensus"
    


