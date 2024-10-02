# Questão 1

def fibonacci(numero):
    a, b = 0, 1

    # Se o número informado for 0 ou 1, ele já pertence à sequência
    if numero == 0 or numero == 1:
        return True
    
    while b < numero:
        a, b = b, a + b
    
    return b == numero

numeroInformado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificar e exibir se o número pertence à sequência de Fibonacci
if fibonacci(numeroInformado):
    print(f"O número {numeroInformado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numeroInformado} NÃO pertence à sequência de Fibonacci.")
