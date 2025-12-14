# Sequência de Fibonacci:
# a soma de dois elementos define a próxima

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b ## Atribuição de valores a passa receber b e b passa a receber a + b

"""
a comeca valendo 0 e b comeca valendo um
na primeira execucao vai printar o 0
na segunda vai printar 1 pois a acabou de receber o valor de b 

Execucao 1
0
a = 1
b = 0 + 1

Execucao 2
1 
a = 1
b = 2

Execucao 3
1
a = 2
b = 3

Explicacao da IA

Inicialmente, a = 0 e b = 1.

Em cada iteração do laço, o valor de `a` é impresso.
Em seguida ocorre a atribuição múltipla `a, b = b, a + b`,
onde o Python primeiro calcula os valores do lado direito
e só depois os atribui às variáveis.

Execução 1:
print(a) → 0
a recebe b → a = 1
b recebe a + b (valores antigos) → b = 1

Execução 2:
print(a) → 1
a recebe b → a = 1
b recebe a + b → b = 2

Execução 3:
print(a) → 1
a recebe b → a = 2
b recebe a + b → b = 3

As expressões do lado direito são avaliadas da esquerda para a direita.

"""