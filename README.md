# 🏦 Controle Bancário em Python

![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg) ![Status](https://img.shields.io/badge/Status-Completed-green)

Bem-vindo ao **Controle Bancário em Python**! Este é um projeto simples que simula um sistema de controle bancário. Aqui você pode realizar operações básicas como **Depósito**, **Saque** e **Extrato**.

## 📋 Funcionalidades

- 📥 **Depósito:** Permite ao usuário adicionar saldo à conta.
- 💸 **Saque:** Realize saques respeitando limites diários e de saldo.
- 📜 **Extrato:** Visualize um resumo de todas as transações realizadas.
- ❌ **Saída:** Encerre a operação do sistema.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+** 🐍
  - Estruturas de controle como `while`, `if-elif-else`
  - Operações com strings e números float
  - Interação via `input()` e `print()`

## 🎯 Objetivo

Este projeto tem o objetivo de praticar conceitos fundamentais de programação Python como loops, condicionais e manipulação de dados. Ele foi desenvolvido como parte de um **exercício prático** para consolidar as aulas do Bootcamp Python Developer, da DIO.

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3.12+** instalado em sua máquina.

2. Clone o repositório:
    ```bash
    git clone https://github.com/mykaelmnzs/Sistema-Bancario.git
    ```
3. Acesse a pasta do projeto:
    ```bash
    cd BANCO
    ```
4. Execute o script:
    ```bash
    python Sistema_Bancario.py
    ```

## 🎉 Exemplo de Execução

```bash
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> d
Informe o valor do depósito: 1000
Depósito: R$ 1000.00

=> s
Informe o valor do saque: 500
Saque: R$ 500.00

=> e
================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 500.00

Saldo: R$ 500.00
=========================================
