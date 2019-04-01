from datetime import datetime

class Jogo:
    def __init__(self,nome,genero,lancamento):
        self._nome = nome
        self._lancamento = format(datetime.strptime(str(lancamento),"%d-%m-%Y"),"%d-%m-%Y")
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

jogo = Jogo("calor","trriler","22-11-2001")

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
        list="".join(li)
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
        print(li[b])
        lista.close()
    
    def listar():
        arquivo = open('jogos.txt','r')
        texto = arquivo.readlines()
        for linha in texto :
            print(linha)
        arquivo.close()




    




def jogar(): 
    menu=0
    while menu!=4:

        menu=int(input("Menu: \n \n O que gostaria de fazer? \n \n 1 - adicionar um jogo \n 2 - Buscar um Jogo \n 3 - Excluir um Jogo \n 4 - Sair"))

        if menu==1:
            nome=input("Digite o nome do jogo: ")
            genero=input("Digite o genero do jogo: ")
            lancamento=input("Digite a data de lancamento: ")
            novoJogo=jogoDAO()
            novoJogo.inserir(jogo)
        
        if menu==2:
            codigo=input("Digite o codigo para buscar as informações")

        



novoJogo=jogoDAO()
#print(jogo)
#novoJogo.inserir(jogo)
#novoJogo.remover(5)
novoJogo.buscar(33)
novoJogo.listar()


