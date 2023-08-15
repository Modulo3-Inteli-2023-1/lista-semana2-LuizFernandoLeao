#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui

def conta_palavras_unicas(frase):
    # Dividir a frase em palavras
    palavras = frase.split()

    # Criar um conjunto vazio para armazenar palavras únicas
    palavras_unicas = set()

    # Iterar pelas palavras e adicioná-las ao conjunto de palavras únicas
    for palavra in palavras:
        palavras_unicas.add(palavra)

    # Retornar a contagem de palavras únicas
    return len(palavras_unicas)

# Uso da função:
frase = "Teste oi eae oi oi ola"
quantidade_palavras_unicas = conta_palavras_unicas(frase)
print(quantidade_palavras_unicas)

# Teste a sua função aqui (caso ache necessário)
