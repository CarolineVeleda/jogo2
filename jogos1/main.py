from classejogos import *
from jogosDAO import *

def jogar(): 
    #menu=0
    #while menu!=4:
        while True:
            try:
                menu=int(input("Menu: \n \n O que gostaria de fazer? \n \n 1 - adicionar um jogo \n 2 - Buscar um Jogo \n 3 - Listar \n 4 - Excluir \n"))
            except ValueError:
                print("Comando inválido")
            else:
                if (menu==1):
                    nome=input("Digite o nome do jogo: ")
                    genero=input("Digite o genero do jogo: ")
                    lancamento=input("Digite a data de lancamento: \n \n *A data deve ser escrita no formato: XX-XX-XXXX \n \n")
                
                    try:
                        #datetime.strptime(lancamento,"%d-%m-%Y")
                        jogo=Jogo(nome,genero,lancamento)
                    except BaseException:
                        print("A data não foi escrita de forma correta, tente novamente.")
                    else:
                        jogo=Jogo(nome,genero,lancamento)
                        novoJogo=jogoDAO()
                        novoJogo.inserir(jogo)
                        print("O jogo foi inserido!")

            
                if (menu==2):
                    verificar = True
                    while (verificar):
                        try: 
                            codigo=int(input("Digite o codigo para buscar as informações"))
                        except ValueError:
                            print("Código inválido, digite números")
                        else:
                            verificar = False
                            novoJogo=jogoDAO() 
                            novoJogo.buscar(codigo)


                if (menu==3):
                    novoJogo=jogoDAO()
                    novoJogo.listar()
                

                if (menu==4):
                    verificar = True 
                    while(verificar):
                        try:
                            codigo = int(input("Digite o codigo do Jogo que você deseja remover: \n"))
                        except ValueError:
                            print("Código inválido, digite números")
                        else:
                            novoJogo=jogoDAO()
                            novoJogo.remover(codigo)
                            print("O jogo foi removido")
                            verificar = False




jogar()