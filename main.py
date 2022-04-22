import os,math

r = int(input("Digite o valor do raio: "))
h = int(input("Digite o valor da altura: "))
os.system('clear')
pote = math.pow(r,2)

cone = (3.14*pote)*h/3

print("O volume do cone é: ",cone)


