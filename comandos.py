import os

# Cria uma identidade dentro da rede
def criar_identidade(nome):
    comando = "freechains keys shared '" + nome + "'"
    with os.popen(comando) as processo:
        saida = processo.read()
    
    # Retorna a saída do comando
    return saida

# Posta um texto dentro da rede
def post(texto,chave):
    comando1 = "freechains chains join '$UERJ' " + chave 
    comando2 = "freechains chain '$UERJ' post inline '" + texto + "'"
    os.system(comando1)
    os.system(comando2)

# Consulta todas as mensagens
def leitura_msgs():
    comando1 = "freechains chain '$UERJ' consensus"
    with os.popen(comando1) as processo:
        saida = processo.read()

    saida = saida.split()    
    # Retorna a saída do comando
    return saida

# Descriptografa as mensagens
def descript_msg(hash):
    comando = "freechains chain '$UERJ' get payload " + hash 
    with os.popen(comando) as processo:
        saida = processo.read()
    
    # Retorna a saída do comando
    return saida



