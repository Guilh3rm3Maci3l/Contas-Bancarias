# Relatório do Sistema Bancário

## 1. Como o sistema foi estruturado

O sistema foi construído seguindo o padrão MVC:
- **Modelos:** As classes principais (`Conta`, `Movimentacao`, `Observador`, `LogObservador`) representam os dados e a lógica de negócio.
- **Controlador:** O `ContaController` é responsável por coordenar todas as operações do sistema (abrir conta, depósito, saque, consulta de saldo, extrato, encerramento).
- **Factory:** A classe `ContaFactory` centraliza a criação de novas contas, mantendo flexibilidade para expansão.

Todas as informações das contas e movimentações são armazenadas em memória, utilizando dicionários e listas para facilitar o acesso e manipulação dos dados.

## 2. Quais padrões de projeto foram usados e onde

- **Factory Method:** O padrão aparece na classe `ContaFactory`, chamada pelo controlador para criar novas contas dinamicamente conforme o tipo solicitado.
- **Observer:** As classes `Observador` (abstrata) e `LogObservador` implementam o padrão Observer. Toda operação nas contas dispara eventos para observadores registrados, permitindo logs e futuras integrações.
- **MVC:** O código separa controle, interface e modelos, garantindo organização e facilidade de manutenção.

## 3. Como as operações podem ser testadas

Basta executar o programa principal (`interface.py`/menu):
- **Abrir conta:** Escolher a opção correspondente e informar o número da conta.
- **Depositar / Sacar:** Escolher a opção, informar número, valor e descrição para cada operação.
- **Consultar saldo / extrato:** Selecionar a conta e, para extrato, informar (ou não) uma data inicial para filtrar movimentações.
- **Fechar conta:** Só é permitido se o saldo da conta for zero.
- **Mensagens:** O sistema informa todos os erros (saldo insuficiente, formato de conta inválido, etc.) e confirma ações corretas em cada etapa.

A interação e resultados são exibidos no terminal, dispensando configurações adicionais.

---
