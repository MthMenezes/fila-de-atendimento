from collections import deque
import time
'''
Váriaveis criada para armazenar:
    fila = deque()  (listas com informações dos cliente)
    cliente = {}  (informações dos clientes)
    orderTimeList = {}  (tempos de produção)
    orderList = []  (armazenar estatisticas finais)
    orderID = 0 (dar um identificador ao pedido)
'''
fila = deque()
fila_prioridade = deque()
cliente = {}
orderTimeList = {}
order_list = []
order_ID = 0
button_final = 0
n = 0

def entrar_fila():
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
            fila_prioridade.append(cliente)
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
              
def start_service():
    '''
    Função criada para realizar os pedidos, calcular o tempo que demorou para serem concluidos e retirar os pedidos ja concluidos da lista. 
    '''
    order_size = len(fila[0]['Pedido'])
    global order_ID 
    order_ID += 1

    cliente_name = fila[0]['Cliente']
    order_name = fila[0]['Pedido']
    print(f'\n---------- Pedido {order_ID} ----------\nAguarde um instante, {cliente_name.capitalize()}.\nLogo seu pedido estará pronto!\n')
    '''
    Como é apenas uma simulação de como funcionaria um aplicativo de pedidos, usei o numero de strings armazenada na na função "orderSize" para usar a função time.sleep()
    e ter um tempo diferente para cada pedido
    '''
    start_time = time.perf_counter()
    time.sleep(order_size)
    endTime = time.perf_counter()
    totalTime = float(endTime) - float(start_time)

    end_order(order_name, totalTime) # Função utilizada para retirar o primeiro cliente da fila.
    

def end_order(orderName, totalTime):
    '''
    Função criada para retirar cliente da fila, onde captura e armazena, em um dicionário, as seguintes informações:
        ID do pedido
        Pedido ja concluidos
        Tempo de produção de cada pedido
    '''
    finish_order = fila.popleft()
    order_num = 'Pedido ' + str(order_ID)
    
    order_time_list = {
        'ID': order_num,
        'Pedido': orderName,
        'Tempo': totalTime
    }

    order_list.append(order_time_list)
    print(f'Seu pedido ficou pronto em apenas {totalTime:.2f} segundos!\n')

def show_done_order(n):
    '''
    Função criada para exibir as estatisticas finais do dia
    '''
    print('---------- ESTÁTISTICAS DO DIA ----------\n')
    for order_time_list in order_list:
        print(f'          {order_list[n]['ID']}          \n     Pedido: {order_list[n]['Pedido'].capitalize()}\n     Tempo: {order_list[n]['Tempo']:.2f} segundos\n----------')
        n += 1
    
while True:
    # Laço criado para adicionar pessoas na fila.
    print(fila)
    print(fila_prioridade)
    entrar_fila()
    start = int(input('\nPosso começar a preparar os pedidos?\n [1]Sim\n [2]Não\n  '))
    if start == 1:
        fila = fila_prioridade + fila
    while start == 1 :
        
        while len(fila) > 0:
            # Laço criado para funcionar enquanto houver clientes na fila.
            start_service()            
        
        if len(fila) == 0: 
            # Quando não tiver mais pessoas na fila, o usuário tem as opções de finalizar o programa ou reiniciar para adicionar mais pessoas a fila.   
            fila_prioridade.clear()
            button_final = int(input('\nTodos pedidos foram concluidos.\n [1]Fechar loja e ver estatísticas do dia\n [2]Adicionar mais pessoas na fila\n  '))    
        if button_final == 1 or 2:
            break
    if button_final == 1:
        break        

show_done_order(n)
