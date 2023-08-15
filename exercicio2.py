#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui

def is_anagram(str1, str2):
    # Removendo espaços e convertendo para letras minúsculas para facilitar a comparação
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Convertendo as strings para listas para permitir a ordenação
    str1_list = list(str1)
    str2_list = list(str2)
    
    # Ordenando as listas
    str1_list.sort()
    str2_list.sort()
    
    # Comparando as listas ordenadas
    return str1_list == str2_list

# Uso da função
print(is_anagram("Amor", "Roma"))  
print(is_anagram("Pedra", "Padre")) 
print(is_anagram("Perda", "Pedra"))  

# Teste a sua função aqui (caso ache necessário)
