import comandos as c
import os 
canal = "UERJ"
key = ""
op = 0
def menu():
    print("\n=== fofocaAE Menu ===")
    print("1. Criar identidade")
    print("2. Ver fofocas")
    print("3. Postar uma fofoca")
    print("4. Comentar uma fofoca")
    print("5. Ver comentarios de uma fofoca")
    print("6. Dar like em fofoca")
    print("7. Dar dislike em fofoca")
    print("8. Sair")

while(op != '8'):
    menu()
    op = str(input("Digite uma opcao: "))

    if(op == '1'):
        os.system("clear")
        nome = str(input("Digite a identidade que deseja usar: "))
        key = c.criar_identidade(nome)
        print("Sua identidade: "+key)
    elif(op == '2'):
        os.system("clear")
        msgs = c.leitura_msgs(canal)
        for i in range(1,len(msgs)):
            print("Fofoca: ",i," - ",c.descript_msg(msgs[i],canal))
    elif(op == '3'):
        os.system("clear")
        if (key != ""):
            fofoca = str(input("Conte-me uma fofoca: "))
            c.post(fofoca,key,canal)
            os.system("clear")
            print("Fofoca enviada")
        else:
            print("Crie uma identidade para comecar a fofocar")
    elif(op == '4'):
       os.system("clear")
       print("Tamo no 4")

    elif(op == '5'):
       os.system("clear")
       print("Tamo no 5")

    elif(op == '6'):
        os.system("clear")
        print("Tamo no 6")

    elif(op == '7'):
       os.system("clear")
       print("Tamo no 7")
       
    elif(op == '8'):
        os.system("clear")
        print("Finalizando...")
    else:
        os.system("clear")
        print("Opcao invalida")