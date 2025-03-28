# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar o CSV
df = pd.read_csv("C://Users//Jucieu//Downloads//INTITUIVE CARE//Projeto - Intituive Care//Python//Python//Relatorio_cadop (3).csv")  # Substitua com o caminho do seu arquivo CSV

@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.get('query', '')  # Pega o termo de busca passado como query string

    # Filtra o dataframe com base no termo de busca, procurando pelo termo em todas as colunas
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    
    # Converte para dicionário e retorna a resposta em JSON
    result = filtered_df.to_dict(orient="records")
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
