# Extrator de Dados de Usinas

Este projeto contém um script em Python que filtra dados de um arquivo CSV com base em nomes de usinas fornecidos pelo usuário e salva os dados filtrados em um arquivo Excel.

## Funcionalidades

- Filtra os dados de um arquivo CSV com base em uma coluna específica (`SIGLA_USINA`).
- Permite ao usuário inserir os nomes das usinas a serem filtradas.
- Processa arquivos CSV grandes em pedaços (chunks) para evitar problemas de memória.
- Salva os dados filtrados em um arquivo Excel no formato `.xlsx`.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/MatheusSMarruda/extrator_de_arquivos.git
   cd extrator_de_arquivos
