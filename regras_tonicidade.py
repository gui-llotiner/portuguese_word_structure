word = str(input('Digite a palavra: ')).lower()
word0 = word.removesuffix('s')
word1 = word0[:-2]
word2 = word0[:-3]

# Listas de Terminações
vogox = ['á', 'é', 'ê', 'i', 'í', 'ó', 'ô', 'u', 'ú', 'ã',
         'ão', 'õe', 'ãe', 'ém']
conox = ['r', 'l', 'z', 'x', 'om', 'im', 'um']
vogpro = ['á', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'ú']
vogsim = ['a', 'e', 'o']
excecao = ['ã']

# Grupos de Palavras

grupo_a = word0.endswith(tuple(vogox)) #Termina em elementos oxitonos
grupo_b = word0.endswith(tuple(conox)) #Termina em consoante
grupo_c = bool(set(vogpro) & set(word0)) #Contém vogal acentuada
grupo_d = word0.endswith(tuple(vogsim)) #Termina em vogal não-acentuada
grupo_e = bool(set(vogpro) & set(word1)) #Contém vogal acentuada (não terminal -2)
grupo_f = bool(set(excecao) & set(word0)) #Contém ã
grupo_g = bool(set(vogpro) & set(word2)) #Contém vogal acentuada (não terminal -3)

# Respostas - Vogais
if (grupo_c and grupo_d and grupo_g == True) and grupo_f == False:
    print('Essa palavra é proparoxítona')
elif grupo_a == True and grupo_e == False:
    print('Essa palavra é oxítona')

# Respostas - Consoantes

elif grupo_b == True and grupo_c == False:
    print('Essa palavra é oxítona')

elif grupo_b and grupo_c == True:
    print('Essa palavra é paroxítona')

else:
    print('Essa palavra é paroxítona')
