from classejogos import *

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
        b=0
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
