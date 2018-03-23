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
            texto = "%s%s\n" % (texto, linha)
            linha = c
    texto = "%s%s" % (texto, linha)
    print(texto)

if __name__ == "__main__":
    texto = sys.argv[1]
    if len(sys.argv) < 3:
        print("exemplo de entrada: python3 string_parte1.py 'texto' [quantidade]")
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
