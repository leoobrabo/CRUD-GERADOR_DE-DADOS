def separar_por_linha():
    print('-'*82)


def vermelho(palavra):
    print(f'\u001b[31m{palavra}\u001b[0m')


def verde(palavra):
    print(f'\u001b[32m{palavra}\u001b[0m')


def amarelo(palavra):
    print(f'\u001b[33m{palavra}\u001b[0m')


def azul(palavra):
    print(f'\u001b[34m{palavra}\u001b[0m')


def apresentar_programa():
    separar_por_linha()
    print('''\u001b[32m
   ______                    __                  __            __          __          
  / ____/__  _________ _____/ /___  _____   ____/ /__     ____/ /___ _____/ /___  _____
 / / __/ _ \/ ___/ __ `/ __  / __ \/ ___/  / __  / _ \   / __  / __ `/ __  / __ \/ ___/
/ /_/ /  __/ /  / /_/ / /_/ / /_/ / /     / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
\____/\___/_/   \__,_/\__,_/\____/_/      \__,_/\___/   \__,_/\__,_/\__,_/\____/____/ 

 \u001b[0m''')
    print(' '*27 + 'Pronto para começar a gerar dados?')
    separar_por_linha()
