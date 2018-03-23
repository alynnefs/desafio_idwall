# -*- coding: utf-8 -*-
import sys

def tratar(texto,quantidade):
    b=texto.split(' ')
    linha=''
    texto=''
    for c in b:
        if len(linha) + len(c) < quantidade:
            linha = "%s %s" % (linha, c) if linha != '' else c
        else:
            linha = justificar(linha,quantidade)
            texto = "%s%s\n" % (texto, linha)
            linha = c
    texto = "%s%s" % (texto, linha)
    print(texto)


def justificar(linha,quantidade):
    extra = quantidade-len(linha)
    existente = len(linha.split(' '))-1
    resto = extra % existente
    aux = ''

    if extra == 0:
        aux = linha
    elif extra > existente:
        j = 0
        while resto > 0:
            aux +=  linha.split(' ')[j] + ' '*((extra//existente)+2)
            resto -= 1
            j += 1
        while j < len(linha.split(' ')):
            aux +=  linha.split(' ')[j] + ' '*((extra//existente)+1)
            j += 1
    elif extra < existente:
        j = 0
        while resto > 0:
            aux +=  linha.split(' ')[j] + ' '*2
            resto -= 1
            j += 1
        while j < len(linha.split(' ')):
            aux +=  linha.split(' ')[j] + ' '
            j += 1
    else: #extra == existente
        j = 0
        while j < len(linha.split(' ')):
            aux +=  linha.split(' ')[j] + ' '*2
            j += 1
    return aux

if __name__ == "__main__":
    texto = sys.argv[1]
    if len(sys.argv) < 3:
        print("exemplo de entrada: python3 string_parte2.py 'texto' [quantidade]")
    else:
        if (int(sys.argv[2]) < 40 and int(sys.argv[2]) < len(sorted(texto.split(' '))[-1])) or int(sys.argv[2]) > 40:
            #if quantidade < len(sorted(texto.split(' '))[-1]):
            print("\nValor inválido. O tamanho usado será 40.\n")
            quantidade = 40
        else:
            quantidade = int(sys.argv[2])
        try:
            for t in texto.split('\n'):
                tratar(t,quantidade)
        except:
            print("\nnão foi dessa vez")
