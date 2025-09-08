'''
 Use uma fila para simular atendimento de clientes.
 Use uma pilha para controlar uma sequência de tarefas.
 Apresente estatísticas ao final (número de atendimentos concluídos e de tarefas pendentes).
 Coleta de tempo de execução com o módulo time.
 Implementação de fila circular ou fila de prioridade.
 Uso de listas aninhadas ou dicionários para armazenar dados adicionais.
'''
from collections import deque
import time

fila = deque()
cliente = {}
orderTimeList = {}
orderList = []
orderID = 0
buttonFinal = 0
n = 0

def entrarFila():
    '''
    Função criada para adicionar cliente na fila, onde captura e armazena, em um dicionário, as seguintes informações:
        Nome
        Pedido
        Prioridade(Criado para identificar se o cliente é portador de alguma condição especial ou não para entrar em uma fila de prioridade)
    ''' 
    name = input('\nDigite o nome do cliente para coloca-lo na fila: ')
    order = str(input(f'\nDigite todos pedidos deste cliente: '))
    while True:
        '''
        Laço criado para obrigar o programa a capturar a informação se o cliente possui ou não uma condição especial
        '''      
        prio = int(input('\nEste cliente é portador de alguma condição especial para colocalo na fila preferencial?\n [1]Sim\n [2]Não\n  ')) 
        if prio == 1:   
            cliente = {
                'Cliente': name,
                'Pedido': order,
                'Prioridade': prio
            }
            fila.appendleft(cliente)
            break
        elif prio == 2:
            cliente = {
                'Cliente': name,
                'Pedido': order,
                'Prioridade': prio
            }
            fila.append(cliente)
            break
        else:
            print('\n---------- Selecione uma opção válida para prosseguir para o atentimento ----------')
              
def startService():
    '''
    Função criada para realizar os pedidos, calcular o tempo que demorou para serem concluidos e retirar os pedidos ja concluidos da lista. 
    '''
    orderSize = len(fila[0]['Pedido'])
    global orderID 
    orderID += 1

    clienteName = fila[0]['Cliente']
    orderName = fila[0]['Pedido']
    print(f'\n---------- Pedido {orderID} ----------\nAguarde um instante, {clienteName.capitalize()}.\nLogo seu pedido estará pronto!\n')
    '''
    Como é apenas uma simulação de como funcionaria um aplicativo de pedidos, usei o numero de strings armazenada na na função "orderSize" para usar a função time.sleep()
    e ter um tempo diferente para cada pedido
    '''
    startTime = time.perf_counter()
    time.sleep(orderSize)
    endTime = time.perf_counter()
    totalTime = float(endTime) - float(startTime)

    endOrder(orderName, totalTime) # Função utilizada para retirar o primeiro cliente da fila.
    

def endOrder(orderName, totalTime):

    finishOrder = fila.popleft()
    orderNum = 'Pedido ' + str(orderID)
    
    orderTimeList = {
        'ID': orderNum,
        'Pedido': orderName,
        'Tempo': totalTime
    }

    orderList.append(orderTimeList)
    print(f'Seu pedido ficou pronto em apenas {totalTime:.2f} segundos!\n')

def showDoneOrder(n):
    print('---------- ESTÁTISTICAS DO DIA ----------\n')
    for orderTimeList in orderList:
        print(f'          {orderList[n]['ID']}          \n     {orderList[n]['Pedido'].capitalize()}\n     {orderList[n]['Tempo']:.2f}\n----------')
        n += 1
    
while True:
    # Laço criado para adicionar pessoas na fila.
    entrarFila()
    start = int(input('\nPosso começar a preparar os pedidos?\n [1]Sim\n [2]Não\n  '))

    while start == 1 :
        
        while len(fila) > 0:
            # Laço criado para funcionar enquanto houver clientes na fila.
            startService()            
        
        if len(fila) == 0: 
            # Quando não tiver mais pessoas na fila, o usuário tem as opções de finalizar o programa ou reiniciar para adicionar mais pessoas a fila.   
            buttonFinal = int(input('\nTodos pedidos foram concluidos.\n [1]Fechar loja e ver estatísticas do dia\n [2]Adicionar mais pessoas na fila\n  '))    
        if buttonFinal == 1:
            break
    if buttonFinal == 1:
        break        

showDoneOrder(n)