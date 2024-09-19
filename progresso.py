import time

total = 50  # Número total de iterações
comprimento_barra = 30  # Comprimento visual da barra

for i in range(total + 1):
    porcentagem = (i / total) * 100
    preenchido = int(comprimento_barra * i // total)
    barra = '█' * preenchido + '-' * (comprimento_barra - preenchido)
    
    print(f'\r|{barra}| {porcentagem:.2f}% Concluído', end='\r')
    time.sleep(0.1)

print()
