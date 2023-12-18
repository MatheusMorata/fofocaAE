import os
# Cria uma identidade dentro da rede do freechains
def criar_identidade(nome):
    comando = "freechains keys shared '" + nome + "'"
    os.system(comando)

def post(texto,chave):
    comando1 = "freechains chains join '$UERJ' " + chave 
    comando2 = "freechains chain '$UERJ' "
    os.system(comando1)
    os.system(comando2)

#os.system("freechains chains join '$UERJ' 96700ACD1128035FFEF5DC264DF87D5FEE45FF15E2A880708AE40675C9AD039E")
#os.system("freechains chain '$UERJ' post inline 'Vascao' ")
#os.system("freechains chain '$UERJ' consensus")
#os.system("freechains chain '$UERJ' get payload 1_C8B17435796755D4F88126BD26A64303BC22D13CE49907AF391165E22A0AA19C")