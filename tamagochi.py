# Utilização de bibliotecas, módulo sleep da biblioteca time para fazer o controle do tempo e leitura de jogo,
# já o módulo randint sorteia alguns números permitindo um desgaste aleatório de pontos dos status.
from time import sleep
from random import randint

# A classe Tamagochi então utilizada para conter os atributos e métodos necessários.
# Inicialmente o usuário começa com os pontos de status já pré-definidos atribuitos para a classe Tamagochi.
class Tamagochi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.energia = 50
        self.diversao = 50
        self.higiene = 50
        self.saude = 100

# Métodos foram criados para cumprir funções de fato dentro do jogo, funções que impactam nos status e eventos do jogo,
# de acordo com as escolhas do usuário, neste caso são comer, dormir, brincar e limpar. 
# Cada uma desenha o pet e retorna os valores impactados na escolha.
    
    def comer(self):
        if self.fome == 100:
            print(f'{self.nome} já está alimentado!')

        else:
            sleep(1.5)
            print('  /\_/\  \n' 
' ( -.- ) \n'
'  > ^ < ')
            print('Nham nham...')
            sleep(1)
            self.fome += 10
            self.energia -= 10
            print(f'Fome +20\nEnergia -10')
    
    def dormir(self):
        if self.energia == 100:
            print(f'{self.nome} não está cansado!')

        else:
            sleep(1.5)
            print('  /\_/\  \n'
' ( -.- ) \n'
'  > ^ <  Zzz ')
            print('ZzZzz...')
            sleep(1)
            print(f'{self.nome} acordou!\nEnergia +100')
            self.energia = 100
    
    def brincar(self):
        if self.diversao == 100:
            print(f'{self.nome} já brincou bastante!')
        
        else:
            sleep(1.5)
            print('  /\_/\  \n'
                ' ( ^_^ ) \n' 
                '  > ^ < '
)
            print('Se divertindo...')
            sleep(1)
            self.diversao += 10
            self.energia -= 10
            print('Diversão +20\nEnergia - 10')
    
    def limpar(self):
        if self.higiene == 100:
            print(f'{self.nome} não está sujo!')
        
        else:
            sleep(1.5)
            print('  /\_/\  \n' 
' ( -.- ) \n'
'  > ^ < ')
            print('Hora do banho...')
            sleep(1)
            self.higiene = 100
            self.energia -= 10
            print(f'{self.nome} está cheirosinho\n +100 Higiene')

# Método retorna_status é responsável por passar ao usuário como está o seu pet virtual
    def retorna_status(self):
        print(f'{"-=" * 3}Status de {self.nome}{"-=" * 3}\nFome: {self.fome}\nEnergia: {self.energia}\nDiversão: {self.diversao}\nHigiene: {self.higiene}\nSaúde: {self.saude}')

# Método verifica_estado verifica se o pet virtual possui algum status zerado porém com saúde maior que 0,
# Caso cumpra esses requisítos o método então subtrai 50 do status saúde,
# Essa condicional evita que a saúde atinja valores negativos.
    def verifica_estado(self):
        if self.fome == 0 and self.saude > 0:
            print(f'\n{self.fome} está faminto!\nSaúde -50')
            self.saude -= 50
            sleep(5) 

        if self.energia == 0 and self.saude > 0:
            print()
            print(f'{self.nome} desmaiou!\nSaúde -50\nEnergia +50')
            self.saude -= 50
            self.energia += 50
            print()
            sleep(5)
        
        if self.diversao == 0 and self.saude > 0:
            print(f'\n{self.nome} está infeliz!\nSaúde -50')
            self.saude -= 50
            sleep(5)
        
        if self.higiene == 0 and self.saude > 0:
            print(f'\n{self.nome} está imundo!\nSaúde -50')
            self.saude -= 50
            sleep(5)

        if self.saude == 0:
            print()
            print( '  /\_/\ \n'  
' ( x_x ) \n'
 '  > ^ <'
)
            print(f'Devido a falta de cuidado {self.nome} não sobreviveu...\nTente novamente!')
            sleep(1)
    
# Método regras passa as regras de jogo para o usuário.
    def regras(self):
        print('Regras do jogo:\n'
              '1 - Os atributos chegam no máximo em 100\n'
              '2 - O mínimo dos atributos é 0, podendo causar algumas reações no pet\n'
              '3 - Se algum atributo chegar a 0 o pet perde 50 de saúde\n'
              '4 - Se a saúde do seu pet chegar a 0 você perde o jogo.\n')   
        sleep(7)    

# Método dá continuidade no jogo e faz o vínculo das opções escolhidas pelo usuário com os métodos definidos para a classe.
# Permite também encerrar o programa caso o usuário deseje, além de fazer um uso geral de métodos também aqui se aplica o uso do módulo randint.
    def roda_jogo(self):
        print(f'\nBem vindo ao Tamagochi!\nJogo desenvolvido por Ryan.')   
        sleep(3)        
        self.retorna_status()
        while True:
            print()
            opcao = int(input('[0] Comer\n[1] Dormir\n[2] Brincar\n[3] Tomar banho\n[4] Regras do jogo\n[5] Sair do programa\nO que deseja fazer? '))
            print()
            if opcao == 0:
                self.comer()
                sleep(3)
            elif opcao == 1:
                self.dormir()
            elif opcao == 2:
                self.brincar()
            elif opcao == 3:
                self.limpar()
            elif opcao == 4:
                self.regras()
            elif opcao == 5:
                print('Finalizando...')
                sleep(1)
                print('Obrigado por jogar!')
                sleep(1)
                break
            else:
                print('Opção inválida, tente digitar o número correspondente a função!')
                continue

# Usa o randint para sortear um status para perder pontos, exigindo assim uma atenção e mannutenção frequente do usuário nos pontos perdidos.
# Permite perder fome, diversão e higiene, não toca em outros pontos pois a energia é perdida a cada escolha e a sáude é fundamental para o pet virtual.
# Além disso o programa também leva em conta a opção escolhida pelo usuário na rodada para não tirar pontos de um elemento que deveria somar, 
# afim de não prejudicar a experiência final.
            sorteio = randint(0, 2)
            if sorteio == 0 and opcao != 0:
                self.fome -= 10
            
            elif sorteio == 1 and opcao != 2:
                self.diversao -= 10
            
            elif sorteio == 2 and opcao != 3:
                self.higiene -= 10
            
            self.verifica_estado()
            if self.saude == 0:
                break
            self.retorna_status()

# O programa coleta o nome do pet virtual escolhido pelo usuário e armazena na memória do atributo nome da classe Tamagochi. 
nome_tamagochi = str(input('Digite o nome do seu pet virtual: '))
tamagochi_usuario = Tamagochi(nome_tamagochi)
# O código tenta executar o jogo normalmente, caso ocorra um erro de valores(ex: Esperado inteiro, digitado uma letra "string")
# O programa então retorna a excessão imprimindo qual seria o erro para o usuário.
try:
    tamagochi_usuario.roda_jogo()
except ValueError:
    print('ERRO, VALOR FORA DO ESPERADO!')