# Teste de API - Vue.js + Python (Flask)

Este repositório contém a implementação de uma aplicação simples com backend em **Python** utilizando **Flask** e frontend em **Vue.js**. O objetivo é realizar uma busca textual em uma lista de operadoras de planos de saúde a partir de um arquivo **CSV** fornecido pela ANS.

---

## Estrutura do Projeto

### Backend (Python - Flask)
- **`app.py`**: Script Python que implementa a API para realizar a busca nas operadoras a partir do arquivo CSV.
- **`requirements.txt`**: Contém as dependências necessárias para rodar o servidor backend, como Flask e pandas.

### Frontend (Vue.js)
- **`/src/App.vue`**: Componente Vue.js responsável pela interface do usuário para realizar a busca de operadoras.
- **`/src/main.js`**: Arquivo que inicializa a aplicação Vue.js.

### Dados
- **`/dados/operadoras_ativas.csv`**: Arquivo CSV que contém os dados das operadoras ativas, como nome, CNPJ, endereço, entre outros.

### Postman
- **`postman_collection.json`**: Coleção do Postman para testar a API. Contém requisições para buscar operadoras com base em um termo de pesquisa.

---

## Como Executar

### Backend (Python - Flask)

1. **Instalar as dependências do backend:**

   Antes de rodar o servidor Python, instale as dependências listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
