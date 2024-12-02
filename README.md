# 🗓️ Organizador de Férias

O **Organizador de Férias** é uma aplicação simples em Python projetada para ajudar empresas a organizar o fluxo de férias dos funcionários, trazendo mais **justiça** e **clareza** no planejamento. Ele segue a lógica de quem entrou primeiro na empresa, garantindo que todos saibam sua vez sem sobrecarga de trabalho para os colegas.

---

## 📋 Como funciona?

1. **Pré-requisitos**:
   - Você precisará de um ambiente que suporte a execução de código Python. Você pode usar:
     - **VSCode** (Visual Studio Code) – Editor de código recomendado.
     - **Terminal do Windows** ou **Terminal do Linux**.
   
2. **Instalação**:
   - Certifique-se de ter o **Python 3.6 ou superior** instalado. Se não tiver, baixe e instale a versão mais recente [aqui](https://www.python.org/downloads/).
   
3. **Execução**:
   - Para rodar a aplicação, basta seguir os passos abaixo:
   
     1. **Clone o repositório**:
        ```bash
        git clone https://github.com/Quaresm/organizador-ferias.git
        ```
     2. **Acesse a pasta do projeto**:
        ```bash
        cd organizador-ferias
        ```
     3. **Execute o programa**:
        - No VSCode, você pode abrir o terminal integrado e digitar:
          ```bash
          python main.py
          ```
        - Ou, no terminal do Windows/Linux, basta navegar até a pasta onde o projeto foi clonado e rodar o comando acima.

4. **Cadastro dos Funcionários**:
   - Informe o número de funcionários a serem cadastrados (mínimo de 2).
   - Para cada funcionário, insira:
     - **Nome** (apenas letras).
     - **Data de entrada** na empresa no formato `DD/MM/AAAA`.

5. **Validação**:
   - O nome deve conter **apenas letras**.
   - A data deve ser válida e seguir o formato `DD/MM/AAAA`.

6. **Processamento**:
   - O programa ordena os funcionários pela data de entrada e exibe:
     - O próximo funcionário a sair de férias.
     - A lista completa de funcionários na ordem de saída.

---

## ✨ Exemplo de Uso

### **Entrada**:

Bem-vindo ao Organizador de Férias!
Quantos funcionários existem? Obs. digite apenas números, no mínimo dois funcionários: 3
Digite o nome do funcionário 1: João
Digite a data de entrada (formato DD/MM/AAAA) do João: 01/01/2020
Digite o nome do funcionário 2: Maria
Digite a data de entrada (formato DD/MM/AAAA) do Maria: 15/03/2021
Digite o nome do funcionário 3: Carlos
Digite a data de entrada (formato DD/MM/AAAA) do Carlos: 10/06/2020


### **Saída**:

Organização completa!
O próximo a sair de férias é: João

Ordem de saída para férias:
2º: Carlos
3º: Maria

⚙️ Requisitos
Python 3.6 ou superior.
Biblioteca padrão datetime (já incluída no Python).

.
🛠️ Como Executar?
Clone este repositório:
```bash
git clone https://github.com/seu-usuario/organizador-ferias.git
```
Acesse a pasta do projeto:
```bash
cd organizador-ferias
```

Execute o programa:
```bash
python main.py
```
