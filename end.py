import time

for i in range(101):
    print(f"Progresso: {i}%", end='\r')
    time.sleep(0.1)



for i in range(5):
    print(f"Contagem: {i}", end='\r')
    time.sleep(1)
