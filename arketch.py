# Atividade: Árvore de Decisão de Crédito - ArkeTech
# Copiloto: ChatGPT

print("========================================")
print("     ARKETECH - SIMULADOR DE CRÉDITO")
print("========================================")

# Entrada de dados
empresa = input("Digite o nome da empresa: ")
faturamento = float(input("Digite o faturamento mensal (R$): "))
emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))

# Verificação dos valores
if faturamento <= 0 or emprestimo <= 0:
    print("\nErro: o faturamento e o empréstimo devem ser maiores que zero.")

else:
    # Cálculo da parcela em 12 vezes sem juros
    parcela = emprestimo / 12

    # Cálculo do percentual comprometido do faturamento
    percentual = (parcela / faturamento) * 100

    print("\n========== RESULTADO ==========")
    print(f"Empresa: {empresa}")
    print(f"Faturamento mensal: R$ {faturamento:.2f}")
    print(f"Empréstimo solicitado: R$ {emprestimo:.2f}")
    print(f"Parcela mensal: R$ {parcela:.2f}")
    print(f"Percentual do faturamento: {percentual:.2f}%")

    # Árvore de decisão de crédito
    if percentual <= 30:
        print("\nStatus: CRÉDITO APROVADO!")
        print("O comprometimento é de até 30% do faturamento.")

    elif percentual <= 50:
        print("\nStatus: EM ANÁLISE!")
        print("O comprometimento está acima de 30% e até 50%.")

    else:
        print("\nStatus: CRÉDITO RECUSADO!")
        print("O comprometimento ultrapassa 50% do faturamento.")

print("========================================")
print("Obrigado por utilizar o simulador ArkeTech!")