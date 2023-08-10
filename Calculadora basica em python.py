num1 = int(input("Primeiro Valor"))
num2 = int(input("Segundo Valor"))



print('''[1] Somar
[2] Multiplicação
[3] Subtração 
[4] Divisão 
[5] Sair da aplicação'''
)
opção = (input("Qual opção deseja selecionar?"))

if opção == '1':
 print(num1+num2)

elif opção == '2':
 print(num1*num2)

elif opção == '3': 
 print(num1 - num2)
 
elif opção == '4':
    if num2 != 0:
        print(num1 / num2)
    else:
      print("Não é possivel dividir por Zero.")
elif opção == '5':
  print("Saindo da Aplicação")
else: print("Opção inválida")








 
