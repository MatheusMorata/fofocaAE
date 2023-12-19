import os

# Cria uma identidade dentro da rede
def criar_identidade(nome):
    comando = "freechains keys shared '" + nome + "'"
    with os.popen(comando) as processo:
        saida = processo.read()
    
    # Retorna a saída do comando
    return saida

# Posta um texto dentro da rede
def post(texto,chave,canal):
    comando1 = "freechains chains join '$"+canal+"' " + chave 
    comando2 = "freechains chain '$"+canal+"' post inline '" + texto + "'"
    os.system(comando1)
    os.system(comando2)

# Consulta todas as mensagens
def leitura_msgs(canal):
    comando1 = "freechains chain '$"+canal+"' consensus"
    with os.popen(comando1) as processo:
        saida = processo.read()

    saida = saida.split()    
    # Retorna a saída do comando
    return saida

# Descriptografa as mensagens
def descript_msg(hash,canal):
    comando = "freechains chain '$"+canal+"' get payload " + hash 
    with os.popen(comando) as processo:
        saida = processo.read()
    
    # Retorna a saída do comando
    return saida

def like(canal,hash,key):
    comando = "freechains chain '$"+canal+"' like '"+hash+"' --sign='"+key+"'"
    os.system(comando)
    print(comando)

def dislike(canal,hash,key):
    comando = "freechains chain '$"+canal+"' dislike '"+hash+"' --sign='"+key+"'"
    os.system(comando)

