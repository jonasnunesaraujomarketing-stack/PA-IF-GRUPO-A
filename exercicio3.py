# Escrever um programa que o usuário digita um número de 1 a 20
# O programa deverá fazer uma contagem regressiva
# Não permitir que o usuário digite um numero maior que 20 ou menor que 1
# Imprimir uma mensagem de "Acabou a contagem" no final.
# Não permitir digitar letras
        
numero = int(input("Digite um número: "))

if numero < 20 and numero > 1 :
 for i in range (numero, -1,-1):
    print(i)

else:
  print ("Insira um número entre 1 e 20 por favor")
  
