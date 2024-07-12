nome = input("Digite o seu nome? ")
nome = input("Digite o seu endereço? ")
nome = input("Digite o seu telefone? ")

def criarTabela():
    opcao=0
    agenda=[]
    while(opcao!=2):
        opcao=int(input("\nMenu: \n 1-Adicionar \n 2-Listar \n 3-Fim \n \n Escolha uma das opcoes? "))
        match opcao:
            case 1:
                nome=input("Informe seu nome ? ")
                endereco=input("Informe seu endereco? ")
                telefone=input("Digite o seu telefone ( (xx) xxxxx-xxxx)? ")
                agenda.append({"nome":nome, "endereco":endereco, "telefone":telefone})
            case 2:
               
                
                for i in range(len(agenda)):
                   
                    print("Nome:",agenda[i]["nome"]+"| Endereço:",agenda[i]["endereco"]+"| Telefone:",agenda[i]["telefone"])
            case 3:
                break
            case _:
                print("Entrada inválida.")
                continue

def main():
    criarTabela()


main()