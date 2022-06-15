numero_usuario = int(input("Por favor, informe um número inteiro: "))
anterior1 = 1
anterior2 = 0

for n_elemento in range (0, numero_usuario + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_usuario == atual:
        print("Esse número está na sequência de Fibonacci!")
        break
    elif numero_usuario < atual:
        print("Esse número não está na sequência de Fibonacci!")
        break