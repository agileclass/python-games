
import csv
import unittest

def ex_01_ler_arquivo_csv():
    linha = []
    with open('exemplos/planilha.csv', 'r') as ficheiro:
        reader = csv.reader(ficheiro, delimiter=';')
        for row in reader:
            linha.append(row)
    return linha