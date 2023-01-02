# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

matriz = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)] #List Comprehension Matriz
minor_subvector = [ sub for sub in matriz if sum(sub) is not n ]

print(matriz)
print(minor_subvector)
