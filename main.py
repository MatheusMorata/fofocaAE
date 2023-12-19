import comandos as c
import os 
canal = "UERJ"
key = ""
key_pvt = ""
palavra = ''
op = 0


def menu():
    print("\n=== fofocaAE Menu ===")
    print("1. Ver fofocas")
    print("2. Postar uma fofoca")
    print("3. Comentar uma fofoca")
    print("4. Ver comentarios de uma fofoca")
    print("5. Dar like em fofoca")
    print("6. Dar dislike em fofoca")
    print("7. Sair")

while(palavra == ''):
    palavra = str(input("Digite um texto para ser usado como chave: "))
    if(palavra == ''):
        print("Digite um texto")
    else:
        key = c.criar_key(palavra)
        key_pvt = c.criar_pvt(palavra)
        os.system("clear")

while(op != '7'):
    menu()
    op = str(input("Digite uma opcao: "))

    if(op == '1'):
        os.system("clear")
        msgs = c.leitura_msgs(canal)
        for i in range(1,len(msgs)):
            print("Fofoca: ",i," - ",c.descript_msg(msgs[i],canal))
    
    elif(op == '2'):
        os.system("clear")
        fofoca = str(input("Conte-me uma fofoca: "))
        c.post(fofoca,key,canal)
        os.system("clear")
        print("Fofoca enviada")

    elif(op == '3'):
        os.system("clear")
        num_fofoca = int(input("Digite o numero da fofoca que deseja comentar: "))
        # Verifica se a fofoca existe
        if((int(num_fofoca) != 0) and (int(num_fofoca) <= int(len(c.leitura_msgs(canal))))):
            comentario = str(input("Digite o comentario: "))
            canal_comentario = 'comentario'+num_fofoca 
            c.post(comentario,key,canal_comentario)
            os.system("clear")
            print("Comentario enviado")
        else:
            print("Esta fofoca nao existe")
       
    elif(op == '4'):
       os.system("clear")
       num_fofoca = int(input("Digite o numero da fofoca que voce deseja ver: "))
       canal_comentario = "comentario"+str(num_fofoca)
       # Verifica se a fofoca existe
       if((int(num_fofoca) != 0) and (int(num_fofoca) <= int(len(c.leitura_msgs(canal))))):
            msgs = c.leitura_msgs(canal_comentario)
            msgs_fofoca = c.leitura_msgs(canal)
            fofoca_foco = msgs_fofoca[int(num_fofoca)]
            fofoca_foco = c.descript_msg(fofoca_foco,canal)
            print("Comentarios sobre a fofoca: "+fofoca_foco)
            for i in range(1,len(msgs)):
                print("Comentario: ",i," - ",c.descript_msg(msgs[i],canal_comentario))
       else:
            print("Esta fofoca nao existe")
        elif(op == '5'):
        os.system("clear")
        num_fofoca = int(input("Digite o numero da fofoca que voce deseja dar like: "))
        # Verifica se a fofoca existe
        if((int(num_fofoca) != 0) and (int(num_fofoca) <= int(len(c.leitura_msgs(canal))))):
            hash = c.leitura_msgs(canal)
            c.like(canal,hash[num_fofoca],key_pvt)
            os.system("clear")
            print("Like enviado")
        else:
            print("Fofoca nao existe")

    elif(op == '6'):
       os.system("clear")
       num_fofoca = int(input("Digite o numero da fofoca que voce deseja dar dislike: "))
       # Verifica se a fofoca existe
       if((int(num_fofoca) != 0) and (int(num_fofoca) <= int(len(c.leitura_msgs(canal))))):
            hash = c.leitura_msgs(canal)
            c.dislike(canal,hash[num_fofoca],key_pvt)
            os.system("clear")
            print("Dislike enviado")
       else:
            print("Fofoca nao existe")
        
    elif(op == '7'):
        os.system("clear")
        print("Finalizando...")

    else:
        os.system("clear")
        print("Opcao invalida")