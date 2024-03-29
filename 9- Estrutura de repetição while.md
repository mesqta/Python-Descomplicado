## Estrutura de laço:

### O que você deve saber sobre Estrutura de repetição while:
- A estrutura é composta por um cabeçalho, corpo e colchetes.  
- O cabeçalho é responsável por definir a condição de parada do loop.  
- O corpo é o bloco de instruções executadas repetidas enquanto a condição for verdadeira.    
- Os colchetes são usados para delimitar os limites da estrutura.      

#### Exemplo de estrutura "while":
```python
contador = 0
valor_inicial = int(input("Digite um valor inicial: "))
limite = int(input("Digite o limite: "))

print("Enquanto o contador for menor que o limite...")

while contador < limite:
    print(f"Valor atual: {contador}")
    contador += 1

print("Foi!")
```
---
A diferença do `for in range()` pelo `while` é que o `range()` já vem com uma iteração pronta, ou seja, ele já começa da posição zero até ao número especificado.

### Interrompendo repetições while:

- `while True`:
#### Exemplo de código com `while True` interrompido pelo usuário:
```python
n = 2 = 0
while True
    n = int(input('Digite um numero: '))
    if n == 99: # Se o usuario digitar 99, sai do loop
        break
print(f'O dobro de {n} é {n*2}')
```
---

### Interrompendo repetições while
