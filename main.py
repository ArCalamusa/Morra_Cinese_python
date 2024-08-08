import random

SCELTE = ['carta', 'forbici', 'sasso']

print('Ciao, questo è il gico del carta, forbici e sasso!')

nome_giocatore = input('Inserisci il tuo nome: ')

print(f'Benvenuto {nome_giocatore}')

modalita_invincibile = input('Vuoi la modalità INVINCIBILE? ').lower() == 'si'
if modalita_invincibile:
    print('Modalita invincibile attiva')
else:
    print('Modalita invincibile NON attiva')

numero_partite = int(input('Quante partite vuoi giocare?'))

vittorie_giocatore = 0
vittorie_pc = 0

for numero_partita in range(numero_partite):

    #stringa formattata per convertive variabile in stringa
    scelta_giocatore = input(f'Partita {numero_partita +1} - {nome_giocatore}, Scegli tra carta, forbici, sasso: ').lower()
    
    if scelta_giocatore not in SCELTE:
        print('Scelta non consentita, il gioco verrà terminato!')
    else:
        if modalita_invincibile:
            if scelta_giocatore == 'carta':
                scelta_pc = 'sasso'
            elif scelta_giocatore == 'forbici':
                scelta_pc = 'carta'
            elif scelta_giocatore == 'sasso':
                scelta_pc = 'forbici'
                
        else:
            scelta_pc = random.choice(SCELTE)
        print(f'Il pc ha scelto: {scelta_pc}')
            
        if scelta_giocatore == scelta_pc:
            risultato ="Pareggio"
        elif(scelta_giocatore == "carta" and scelta_pc == "sasso") or \
                (scelta_giocatore == "forbici" and scelta_pc == "carta") or \
                (scelta_giocatore == "sasso" and scelta_pc == "forbici"):
            risultato = f'{nome_giocatore} hai vinto!'
            vittorie_giocatore += 1
        else: 
            risultato = 'PC vince!'
            vittorie_pc += 1
            
        print(f'Risultato: {risultato}')
        
    print(f'Punteggio attuale: {nome_giocatore} - {vittorie_giocatore}, Pc - {vittorie_pc}')
    
if vittorie_giocatore > vittorie_pc:
    print(f"{nome_giocatore} è il vincitore finale!")
elif vittorie_giocatore < vittorie_pc:
    print("Il pc è il vincitore finale")
else:
    print("Avete pareggiato!")

print(f'Alla prossima, {nome_giocatore}!')


        