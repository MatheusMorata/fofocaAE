import comandos as c
import os 

key = ""
op = 0
def menu():
    print("\n=== fofocaAE Menu ===")
    print("1. Criar identidade")
    print("2. Ver fofocas")
    print("3. Postar fofoca")
    print("4. Sair")

while(op != '4'):
    menu()
    op = str(input("Digite uma opcao: "))

    if(op == '1'):
        os.system("clear")
        nome = str(input("Digite a identidade que deseja usar: "))
        key = c.criar_identidade(nome)
        print("Sua identidade: "+key)
    elif(op == '2'):
        os.system("clear")
        msgs = c.leitura_msgs()
        for i in range(1,len(msgs)):
            print("Fofoca: ",i," - ",c.descript_msg(msgs[i]))
    elif(op == '3'):
        os.system("clear")
        if (key != ""):
            fofoca = str(input("Conte-me uma fofoca: "))
            c.post(fofoca,key)
            os.system("clear")
            print("Fofoca enviada")
        else:
            print("Crie uma identidade para comecar a fofocar")
    elif(op == '4'):
        os.system("clear")
        print("Finalizando...")
    else:
        os.system("clear")
        print("Opcao invalida")