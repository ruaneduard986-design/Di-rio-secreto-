import time
print("iniciando o programa...")
time.sleep(5)
print("programa inciado")
pergunta = input("Qual é a senha:")
senha = "123"
if pergunta == senha:
  print("acesso liberado")
else:
  print("acesso negado")
  exit()

diario = []

while True:
  print("1 - Escrever no diário")
  print("2 - Ler o diário")
  print("3 - Sair")
  opcao = input("Escolha: ")

  if opcao == "1":
    texto = input("Escreva: ")
    diario.append(texto)
    print("Salvo!")
  elif opcao == "2":
    if len(diario) == 0:
      print("Diário vazio")
    else:
      for i in range(len(diario)):
        print(i + 1, "-", diario[i])
  elif opcao == "3":
    print("Saindo...")
    break
  else:
    print("Opção inválida")