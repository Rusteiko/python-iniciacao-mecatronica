"""# Exercícios

Escreva um programa que leia o nome e a idade aluno. Peça três notas do aluno e exiba a média das notas
"""

# Aula 01 - Exercício 01
nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota --> "))
nota2 = float(input("Informe a segunda nota --> "))
nota3 = float(input("Informe a terceira nota --> "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno {nome} é {media}")
