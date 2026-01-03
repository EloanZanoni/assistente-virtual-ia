print("🤖 Assistente Virtual de Estudos")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Usuário: ")

    if pergunta.lower() == "sair":
        print("Assistente: Até a próxima! Bons estudos!")
        break

    resposta = f"Assistente: Vou te ajudar a entender melhor sobre: {pergunta}. " \
               f"Imagine que você está estudando esse tema pela primeira vez. " \
               f"A explicação deve ser clara, objetiva e com exemplos práticos."

    print(resposta + "\n")
