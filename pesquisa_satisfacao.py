# Pesquisa de satisfação - TudoWeb

excelente = 0
ruim = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")
print()

for entrevistado in range(1, 51):

    print(f"--- Entrevistado {entrevistado} ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nAvalie o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")

    elif opiniao == 2:
        print("Opinião registrada: BOM")

    else:
        ruim += 1
        print("Opinião registrada: RUIM")

    print()

print("=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)