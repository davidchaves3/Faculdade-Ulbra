def contagem_e_extracao(arq):
    arquivo = open(arq, 'r')
    contador_funcoes = 0
    lista_funcoes = []
    funcoes_argumentos = {}
    linhas = arquivo.read().split('\n')
    
    codigo_corrigido = []  # Armazena o código corrigido
    
    for linha in linhas:
        linha = linha.strip()
        
        if linha.startswith("def "):
            if linha.endswith(":"):
                codigo_corrigido.append(linha)
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
            else:
                linha_corrigida = linha + ":"
                codigo_corrigido.append(linha_corrigida)
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
        
        elif linha.startswith(("if ", "elif ", "else ", "for ", "while ")):
            if linha.endswith(":"):
                codigo_corrigido.append(linha)
            else:
                linha_corrigida = linha + ":"
                codigo_corrigido.append(linha_corrigida)
        
        else:
            codigo_corrigido.append(linha)
    
    arquivo.close()
    
    # Escreve o código corrigido em um novo arquivo (programa2.py)
    nome_arquivo_corrigido = "programa2.py"
    arquivo_corrigido = open(nome_arquivo_corrigido, 'w')
    arquivo_corrigido.write("\n".join(codigo_corrigido))
    arquivo_corrigido.close()
    
    return lista_funcoes, contador_funcoes, funcoes_argumentos

