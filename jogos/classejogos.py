from datetime import datetime

class Jogo:
    def __init__(self,nome,genero,lancamento):
        self._nome = nome
        #self._lancamento = format(datetime.strptime(str(lancamento),"%d-%m-%Y"),"%d-%m-%Y")
        #if(isinstance(lancamento, datetime.date)):
            #self._lancamento = lancamento
        
        if(isinstance(lancamento, str)):
            try:
                self._lancamento = format(datetime.strptime(str(lancamento),"%d-%m-%Y"),"%d-%m-%Y")
            except ValueError:
                raise ValueError("O formato da data é inválido.")

        self._genero = genero
        self._cod = ""

    def _get_nome(self):
        return self._nome
    def _get_lancamento(self):
        return self._lancamento
    def _get_genero(self):
        return self._genero
    def _get_cod(self):
        return self._cod
    def _set_nome(self, nome):
        self._nome = nome
    def _set_lancamento(self, lancamento):
        self._lancamento = lancamento
    def _set_genero(self, genero):
        self._genero = genero
    def _set_cod(self, cod):
        self._cod = cod
    
    nome = property(_get_nome,_set_nome)
    genero = property(_get_genero,_set_genero)
    lancamento = property(_get_lancamento,_set_lancamento)
    cod = property(_get_cod,_set_cod)
    
    def __str__(self):
        return "{},{},{}".format(self._nome,self._genero,self._lancamento)




class jogoDAO:    
    def inserir(self,jogo):
        lista=open("jogos.txt","r")
        li=lista.readlines()
        if (len(li)<1):
            jogo.cod=1
        else:
            a=int(li[len(li)-1].split(",")[0])
            jogo.cod=a+1
        li+="{},{},{},{}\n".format(jogo.cod,jogo.nome,jogo.genero,jogo.lancamento)
        li="".join(li)
        k=open("jogos.txt","w")
        k.writelines(li)
        k.close()
        return("jogo registrado")

    def remover(self,cod):
        lista=open("jogos.txt","r")
        li=lista.readlines()
        b= 0
        for n in li:
            codigo = n.split(',')[0]
            if(int(codigo) == int(cod)):
                break
            b+=1
        li.pop(b)
        k=open("jogos.txt","w")
        k.writelines(li)
        k.close()
        return("pessoa removida com sucesso")
        print(li)
    
    def buscar(self,cod):
        lista=open("jogos.txt","r")
        li=lista.readlines()
        b= 0
        for n in li:
            codigo = n.split(',')[0]
            if(int(codigo) == int(cod)):
                break
            b+=1
        
        pos=n.split(',')
        print("As informações são: \n")
        print("Nome:{}, Genero:{}, Lancamento:{}".format(pos[1], pos[2], pos[3]))    
        #print(li[b])
        return li[b]
        lista.close()
    
    def listar(self):
        arquivo = open('jogos.txt','r')
        texto = arquivo.readlines()
        for linha in texto :
            print(linha)
        arquivo.close()

"""  
    def alterar(self,jogo):
        
        antigo=self.buscar(jogo.cod)
        arquivo = open('jogos.txt','r')
        texto = arquivo.readlines()
        v=[]
        for linha in texto:
            linha1 = linha.split(",")
            codigo = linha.split(',')[0]
            if(int(codigo) == jogo.cod):
                linha1=jogo
                break

            v.append(linha1)
        k=open('jogos.txt','w')
        k.writelines(v)
        arquivo.close()
        #print(antigo)
"""





    




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

#jogo=Jogo("JOGO INCRIVEL MEU DEUS UAU","FODA KLEIN","12-12-2019")
#codigo=4
#jogo.cod=codigo
#novoJogo=jogoDAO()
#novoJogo.alterar(jogo)

#print(jogo)
#novoJogo.inserir(jogo)
#novoJogo.remover(5)
#novoJogo.buscar(33)
#novoJogo.listar()


