# Organizador de Férias
from datetime import datetime
def organizar_ferias():
    print("Bem-vindo ao Organizador de Férias!")
    
    while True:
        quantidade_de_funcionarios = input("Quantos funcionários existem? Obs. digite apenas números, no mínimo dois funcinários: ")
        if quantidade_de_funcionarios.isdigit():  # Verifica se o valor é numérico
            quantidade_de_funcionarios = int(quantidade_de_funcionarios)  # Converte para inteiro
            break
        else:
            print("Entrada inválida. Por favor, digite apenas números.")
    
    # Lista para armazenar os funcionários e suas datas de entrada
    funcionarios = []

    # Cadastro dos funcionários e suas datas de entrada
    for i in range(quantidade_de_funcionarios):
        while True:  # Loop para validação dos inputs no cadastro
            nome = input(f"Digite o nome do funcionário {i + 1}: ").strip()
            if not nome.isalpha():  # Verifica se o nome contém apenas letras
                print("O nome deve conter apenas letras. Tente novamente.")
                continue

            data_entrada = input(f"Digite a data de entrada (formato DD/MM/AAAA) do {nome}: ").strip()
            try:
                # Tenta converter a data para o formato correto
                data_convertida = datetime.strptime(data_entrada, "%d/%m/%Y")
            except ValueError:
                print("Data inválida. Por favor, use o formato DD/MM/AAAA.")
                continue

            # Se ambas as entradas forem válidas, adiciona o funcionário à lista
            funcionarios.append({"nome": nome, "data_entrada": data_convertida})
            break
    
    # Ordenando os funcionários pela data de entrada
    funcionarios.sort(key=lambda x: x["data_entrada"])

    # Exibindo os resultados
    print("\nOrganização completa!")
    print(f"O próximo a sair de férias é: {funcionarios[0]['nome']}")
    
   # Listando os demais funcionários a tirarem férias em ordem
    print("\nOrdem de saída para férias:")
    for i, funcionario in enumerate(funcionarios[1:], start=2):  # Exibe do segundo funcionário em diante
        print(f"{i}º: {funcionario['nome']}")


# Executando o programa
organizar_ferias()