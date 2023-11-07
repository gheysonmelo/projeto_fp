import os
os.system('cls')

print('  ~' * 9)
print('     Biblioteca da Nat')
print('  ~' * 9)

# 1.0 Criando a lista 
biblioteca = []

# 1.2 função SALVANDO_EM_CSV:
def salvar_em_csv(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_csv:
        # Escreve o cabeçalho
        arquivo_csv.write("Nome,Autor,Categoria,Preco\n")

        # Escreve os dados
        for livro in lista:
            linha = f"{livro['nome']},{livro['autor']},{livro['categoria']},{livro['preco']:.3f}\n"
            arquivo_csv.write(linha)
nome_arquivo = "bibli.csv"

# 1.3 função ADICIONANDO_LIVRO:
def adicionando_livro():
    while True:
        nome_livro = input('Qual o nome do livro? ')
        
        autor = input('Quem é o autor? ')
        
        categoria = input('Escolha pelo código as seguintes opções: \n[acao] Ação\n[comd] Comédia\n[ficc] Ficção\n[terr] Terror\n[roma] Romance\n[dram] Drama\n Qual categoria escolhida: ')
        
        #Tratamento de erro em categoria, caso tenha adicionado algo errado:
        while True:
            if categoria == 'acao' or categoria == 'comd' or categoria == 'ficc' or categoria == 'terr' or categoria == 'roma' or categoria == 'dram':
                print('Categoria adicionada')
                break
            else:
                categoria = input('Digite uma resposta válida: ')
        
        preco = float(input('Qual o preço do livro? '))

        novo_livro = {'nome': nome_livro, 'autor': autor,'categoria': categoria,'preco': preco} 
        biblioteca.append(novo_livro)

        #Pergunta se deseja adicionar mais outro livro:
        pergunta = input('Nat, você deseja adicionar mais algum livro? [S/N] ')
        
        #Tratamento, caso a resposta fuja do esperado (S ou N):
        if pergunta in 'Ss':
            continue
        elif pergunta in 'Nn':
            break
        else:
            while pergunta not in 'SsNn':
                pergunta = input('Ops... A resposta não é válida. Escreva uma resposta válida: [S/N] ')

#1.5 Fazendo o filtro por categoria
def filtro_categoria(categoria_escolhida):
            with open('bibli.csv', 'r') as arquivo:
                #Linhas lendo e armazenando todas as linhas do arquivo csv
                linhas = arquivo.readlines()

                #Cabecalho -> Guardando apenas a linhas zero, a do cabeçalho
                cabecalho = linhas[0].strip().split(',')

                #Guardando em uma lista as linhas seguintes. Cada linha será uma lista dentro da lista DADOS
                dados = []
                for linha in linhas[1:]:
                    valores = linha.strip().split(',')
                    dados.append(valores)

                #Exibir o cabeçalho e os dados
                print("Cabeçalho:", cabecalho)
                
                
                print("Dados Categoria:")
                
                categoria_encontrada = False
                
                for linha in dados:
                    for categoria in linha:
                        if categoria == categoria_escolhida:
                            categoria_encontrada = True
                            print(linha)
                            break  #O break, neste caso, é para ele parar de procurar, após achar

                if not categoria_encontrada:
                    print(f"A categoria '{categoria_escolhida}' não foi encontrada no arquivo CSV.")

#1.1 Criando o menu:
while True:
    print('Escolha, pelo seu código, as seguintes opções: ')
    print('[1] Listar livros')
    print('[2] Salvar em arquivo .CSV')
    print('[3] Adicionar livro')
    print('[4] Sair')
    print('[5] Filtro de livros por categoria')
    
    #A variável será recebida em string, mesmo que seja um número, pois fica mais fácil de fazer seu tratamento.
    escolha = input('O que deseja: ')
    
    #1.1Visualização da biblioteca
    if escolha == '1':
        if len(biblioteca) < 1:
                print('Ainda não foi adicionado nenhum livro :(\nAdicione um livro na opção [3]')
                print()
        else:
            print()
            print('='*150)
            print(f"{'Código':^30}{'Livro':^30}{'Autor':^30}{'Preço':^30}")
            print('-'*150)

            for codigo, livro in enumerate(biblioteca):
                print(f"{codigo:^30}{livro['nome']:^30}{livro['autor']:^30}{livro['preco']:^30}")
            print('='*150)
            print()
    #1.2Salvando em arquivo CSV
    elif escolha == '2':
        salvar_em_csv(biblioteca, nome_arquivo)
        print(f'Dados salvos no arquivo BIBLI da Nat')

    #1.3Chamando a função ADICIONANDO_LIVRO:
    elif escolha == '3':
        adicionando_livro()
        print()
    
    #1.4Saindo do programa
    elif escolha == '4':
        break
    
    elif escolha == '5':
        categoria_escolhida = input('Está procurando um livro? \nMe diga a categoria escolhida: ')
        filtro_categoria(categoria_escolhida)  
                
    print()
print(f"{'Tchauu Até Mais':^30}")