
class jogoDAO:

    def _inserir (self,jogo):
        """arquivo = open('jogos.txt', 'r')
        lista = "".join(arquivo.readlines())
        obj = lista.split("\n")
        if (len(obj)-1<2):
            obj.cod=1
            arquivo=open('jogos.txt', 'w')
            lista+="{},{},{},{}\n".format(self._cod,self._nome,self._genero,self._lancamento)
            arquivo.writelines(lista)
            arquivo.close()
        else:
            obj.cod=int(obj[len(obj)-1].split(",")[0])+1
            arquivo=open('jogos.txt', 'w')
            lista+="{},{},{},{}\n".format(self._cod,self._nome,self._genero,self._lancamento)
            arquivo.writelines(lista)
            arquivo.close()
        """"
        return "Jogo adicionado!
        
        #arquivo.write(jogo.__"str__()+"\n")
        

    def _listar(self):
        arquivo = open('jogos.txt','r')
        texto = arquivo.readlines()
        for linha in texto :
            print(linha)
        arquivo.close()


def jogar(): 
    menu=0
    while menu!=2:

        menu=int(input("Menu: \n \n O que gostaria de fazer? \n \n 1 - adicionar um jogo \n 2 - Sair \n"))

        if menu==1:
            nome = input('Nome do jogo: ')
            l = input('Digite a data de lançamento: ')
            genero = input('Categoria do Jogo: ')
            lanc=datetime.strptime(l, '%d/%m/%Y').date()
            jogo = Jogo(nome,genero)
            jogo.lancamento = lanc
            novoJogo=jogoDAO()
            novoJogo._inserir(jogo.__str__())
            




#jogar()
#novoJogo._listar()
#novoJogo._excluir("1")