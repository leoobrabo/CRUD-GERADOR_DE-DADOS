import random
from time import sleep
from ultilidades import apresentar_programa, vermelho, verde, azul, amarelo, separar_por_linha

lista_nomes = ['Leonardo', 'Rita', 'Heraclito', 'Luciene', 'Eric']

lista_emails = ['leonardomotta2010@hotmail.com', 'leomotta2777@gmail.com',
                'teste@gmail.com', 'usuario@gmail.com', 'teste@hotmail.com']

lista_telefones = ['99999-0000', '98888-0000',
                   '97777-0000', '96666-0000', '95555-0000']

lista_cidades = ['Brasilia', 'São Paulo',
                 'Rio de Janeiro', 'Minas Gerais', 'Goias']

lista_estados = ['DF', 'SP', 'RJ', 'MG', 'GO']


def salvar_arquivo(dados):
    with open('dados_de_teste.txt', 'a', encoding='utf-8') as arquivo:
        conteudo = f'{dados}\n'
        arquivo.writelines(conteudo)


def escolha_aleatoria():
    aleatorio = random.randint(0, 4)
    return aleatorio


def aviso_de_licenca():
    amarelo('Funcionalidade para assinantes')
    vermelho('Entre em contato com o administrador')
    azul('leonardomotta2010@hotmail.com')
    sleep(2)


def menu():
    print('Ultilize uma ou mais opções para gerar dados aleatorios')

    while True:
        separar_por_linha()
        verde('1 - Para gerar Nomes')
        verde('2 - Para gerar emails')
        verde('3 - Para gerar telefones')
        verde('4 - Para gerar cidades')
        verde('5 - Para gerar estados')
        aleatorio = escolha_aleatoria()
        escolha = input('Digite a Opção Desejada: ')

        if escolha == 'parar':
            amarelo('Finalizando Programa')
            break

        escolhas = escolha.split(',')

        salvar = input('Deseja salvar as opções (s/n)')

        for i in escolhas:
            if i == '1':
                nome = lista_nomes[aleatorio]
                if salvar == 's':
                    print(nome)
                    salvar_arquivo(nome)
                else:
                    print(nome)
            elif i == '2':
                email = lista_emails[aleatorio]
                if salvar == 's':
                    print(email)
                    salvar_arquivo(email)
                else:
                    print(email)
            elif i == '3':
                telefone = lista_telefones[aleatorio]
                if salvar == 's':
                    print(telefone)
                    salvar_arquivo(telefone)
                else:
                    print(telefone)
            elif i == '4':
                cidade = lista_cidades[aleatorio]
                if salvar == 's':
                    print(cidade)
                    salvar_arquivo(cidade)
                else:
                    print(cidade)
            elif i == '5':
                estado = lista_estados[aleatorio]
                if salvar == 's':
                    print(estado)
                    salvar_arquivo(estado)
                else:
                    print(estado)
            else:
                vermelho('Opção Invalida')


def apresentar_menu():
    separar_por_linha()
    verde('1 - Ultilizar o Gerador de dados')
    amarelo('2 - Editar dados existente')
    vermelho('3 - Excluir um dado')
    verde('4 - Criar dado')
    verde('5 - Sair')
    opcao = input('Digite uma opção: ')
    separar_por_linha()
    return opcao


if __name__ == '__main__':
    apresentar_programa()
    while True:
        opcao = apresentar_menu()
        if opcao == '1':
            menu()
        if opcao == '2':
            aviso_de_licenca()

        if opcao == '3':

            aviso_de_licenca()

        if opcao == '4':
            aviso_de_licenca()

        if opcao == '5':
            amarelo('Encerrando aplicação')
            break
