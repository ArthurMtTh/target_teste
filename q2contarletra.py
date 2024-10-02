# Questão 2

import unicodedata

# Normalizar o texto para remover acentos latinos, como: ~, ^, ´, `
def removerAcento(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def contarLetraA(texto):
    # Converter para minúsculas para facilitar a contagem
    textoNormalizado = removerAcento(texto.lower())

    contagem = textoNormalizado.count('a')

    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

textoInformado = input("Informe uma string para verificar a ocorrência da letra 'a': ")
contarLetraA(textoInformado)