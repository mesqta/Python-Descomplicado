from random import shuffle
alu1 = str(input('Aluno 1: '))
alu2 = str(input('Aluno 2: '))
alu3 = str(input('Aluno 3: '))
alu4 = str(input('Aluno 4: '))

lista = [alu1, alu2, alu3, alu4]
alunos = shuffle(lista)

print('A ordem é: ')
print(lista)