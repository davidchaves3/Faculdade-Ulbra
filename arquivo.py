def mensagem(titulo,msg):
    print("=-"*50 )
    print(titulo, ":", msg)
    print("=-"*50 + "\n")

def contagem_e_extracao(arq):
    arquivo = open(arq, 'r')
    contador_funcoes = 0
    lista_funcoes = []
    funcoes_argumentos = {}
    
    linhas = arquivo.read().split('\n')
    
    for linha in linhas:
        linha = linha.strip()
        
        if linha.startswith("def "):
            contador_funcoes += 1
            nome_funcao = linha.split("def ")[1].split("(")[0]
            lista_funcoes.append(nome_funcao)
            
            argumentos = []
            argumentos_str = linha.split("(")[1].split(")")[0]
            
            for argumento in argumentos_str.split(","):
                argumento = argumento.strip()
                
                if argumento:
                    argumentos.append(argumento)
                    
            funcoes_argumentos[nome_funcao] = argumentos
    
    arquivo.close()
    
    return lista_funcoes, contador_funcoes, funcoes_argumentos

nome_arquivo = "arquivo.py"

funções, quantidade_funçoes,parametros = contagem_e_extracao(nome_arquivo)

mensagem("Nomes das Funções:",funções)
mensagem("Qtd de Funções:",quantidade_funçoes)
mensagem("Funções e parametros:",parametros)
