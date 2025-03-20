# -*- coding: utf-8 -*-
# Projeto desenvolvido por Lucas Rial
# Copyright (c) 2025 Lucas Rial. Todos os direitos reservados.

from flask import Flask, render_template, request
import openai
import pyodbc

# Configuração da API do OpenAI
openai.api_key = "SUA CHAVE API OPENAI AQUI"

# Configuração da conexão com o banco de dados Protheus
DB_CONNECTION_STRING = "SUA CONEXAO COM BANCO AQUI"

# Definição de módulos e suas tabelas
MODULOS = {
    "Faturamento": "Tabelas disponíveis: SD2010 (D2_FILIAL (Filial,TP char, TAM 2), D2_ITEM (Item,TP char, TAM 2), D2_COD (Produto,TP char, TAM 15), D2_QUANT (Quantidade,TP num, TAM 11), D2_PRCVEN (Vlr.Unitario,TP num, TAM 14), D2_TOTAL (Vlr.Total,TP num, TAM 14), D2_VALIPI (Vlr.IPI,TP num, TAM 14), D2_VALICM (Vlr.ICMS,TP num, TAM 14), D2_TES (Tipo Saida,TP char, TAM 3), D2_CF (Cod. Fiscal,TP char, TAM 5), D2_DESC (Desc.Item,TP num, TAM 5), D2_IPI (Aliq. IPI,TP num, TAM 5), D2_PICM (Aliq. ICMS,TP num, TAM 5), D2_VALCSL (Valor CSLL,TP num, TAM 14), D2_CONTA (C Contabil,TP char, TAM 20), D2_OP (Ord Producao,TP char, TAM 14), D2_PEDIDO (No do Pedido,TP char, TAM 6), D2_ITEMPV (Item do Ped.,TP char, TAM 2), D2_CLIENTE (Cliente,TP char, TAM 6), D2_LOJA (Loja,TP char, TAM 2), D2_LOCAL (Armazem,TP char, TAM 2), D2_DOC (Num. Docto.,TP char, TAM 9), D2_SERIE (Serie,TP char, TAM 3), D2_EMISSAO (Emissao,TP data, TAM 8), D2_CUSTO1 (Custo,TP num, TAM 14), D2_CCUSTO (Centro Custo,TP char, TAM 9), D2_ITEMCC (Item C.C.,TP char, TAM 9), D2_DESPESA (Vlr. Despesa,TP num, TAM 14), D2_CLVL (Classe Valor,TP char, TAM 9))",
    "Financeiro": "Tabelas disponíveis: SE1010 (E1_FILIAL (Filial,TP char, TAM 2), E1_PREFIXO (Prefixo,TP char, TAM 3), E1_NUM (No. Titulo,TP char, TAM 9), E1_PARCELA (Parcela,TP char, TAM 2), E1_TIPO (Tipo,TP char, TAM 3), E1_NATUREZ (Natureza,TP char, TAM 10), E1_CLIENTE (Cliente,TP char, TAM 6), E1_LOJA (Loja,TP char, TAM 2), E1_NOMCLI (Nome Cliente,TP char, TAM 20), E1_EMISSAO (DT Emissao,TP data, TAM 8), E1_VENCTO (Vencimento,TP data, TAM 8), E1_VENCREA (Vencto real,TP data, TAM 8), E1_VALOR (Vlr.Titulo,TP num, TAM 16), E1_BASEIRF (Base Imposto,TP num, TAM 16), E1_IRRF (IRRF,TP num, TAM 14), E1_ISS (ISS,TP num, TAM 14), E1_NUMBCO (Nº no Banco,TP char, TAM 15), E1_INDICE (Reajuste,TP char, TAM 3), E1_BAIXA (DT Baixa,TP data, TAM 8), E1_EMIS1 (DT Contab.,TP data, TAM 8), E1_HIST (Historico,TP char, TAM 40), E1_VEND1 (Vendedor 1,TP char, TAM 6), E1_MULTA (Multa,TP num, TAM 16), E1_JUROS (Juros,TP num, TAM 16), E1_CORREC (Correcao,TP num, TAM 16), E1_VALLIQ (Vlr.Liq Baix,TP num, TAM 16), E1_VENCORI (Vencto Orig,TP data, TAM 8), E1_FATURA (Fatura,TP char, TAM 9), E1_NUMNOTA (Nota Fiscal,TP char, TAM 9), E1_SERIE (Serie,TP char, TAM 3), E1_STATUS (Status,TP char, TAM 1), E1_ORIGEM (Origem,TP char, TAM 8), E1_VLRREAL (Valor Real,TP num, TAM 16), E1_TRANSF (Doc.Transf.,TP char, TAM 15), E1_INSS (INSS,TP num, TAM 14), E1_CSLL (CSLL,TP num, TAM 14), E1_COFINS (COFINS,TP num, TAM 14), E1_PIS (PIS/PASEP,TP num, TAM 14), E1_MESBASE (Mes Base,TP char, TAM 2), E1_ANOBASE (Ano Base,TP char, TAM 4), E1_CCD (C.Custo Deb.,TP char, TAM 9), E1_ITEMD (Item Ctb.Deb,TP char, TAM 9), E1_CLVLDB (Cl.Vlr. Deb.,TP char, TAM 9), E1_CREDIT (Conta Cred.,TP char, TAM 20), E1_CCC (C.Custo Cred,TP char, TAM 9), E1_ITEMC (It.Ctb.Cred.,TP char, TAM 9), E1_CLVLCR (Cl.Vlr. Cred,TP char, TAM 9), E1_DESCON1 (Desconto,TP num, TAM 15), E1_PARTOT (Parcela atua,TP char, TAM 4)), SE2010 (E2_FILIAL (Filial,TP char, TAM 2), E2_PREFIXO (Prefixo,TP char, TAM 3), E2_NUM (No. Titulo,TP char, TAM 9), E2_PARCELA (Parcela,TP char, TAM 2), E2_TIPO (Tipo,TP char, TAM 3), E2_NATUREZ (Natureza,TP char, TAM 10), E2_PORTADO (Portador,TP char, TAM 3), E2_FORNECE (Fornecedor,TP char, TAM 6), E2_LOJA (Loja,TP char, TAM 2), E2_NOMFOR (Nome Fornece,TP char, TAM 20), E2_EMISSAO (DT Emissao,TP data, TAM 8), E2_VENCTO (Vencimento,TP data, TAM 8), E2_VENCREA (Vencto Real,TP data, TAM 8), E2_VALOR (Vlr.Titulo,TP num, TAM 16), E2_ISS (ISS,TP num, TAM 14), E2_IRRF (IRRF,TP num, TAM 14), E2_INDICE (Reajuste,TP char, TAM 3), E2_BAIXA (DT Baixa,TP data, TAM 8), E2_BCOPAG (Bco de Pgto,TP char, TAM 3), E2_EMIS1 (DT Contab.,TP data, TAM 8), E2_HIST (Historico,TP char, TAM 40), E2_MOTIVO (Motivo,TP char, TAM 20), E2_MOVIMEN (Ult.Moviment,TP data, TAM 8), E2_OP (Ord Producao,TP char, TAM 14), E2_SALDO (Saldo,TP num, TAM 16), E2_OK (Ident.Baixa,TP char, TAM 2), E2_DESCONT (Desconto,TP num, TAM 16), E2_MULTA (Multa,TP num, TAM 16), E2_JUROS (Juros,TP num, TAM 16), E2_VENCORI (Vencto Orig,TP data, TAM 8), E2_VALJUR (Taxa Perman.,TP num, TAM 14), E2_PORCJUR (Porc Juros,TP num, TAM 5), E2_MOEDA (Moeda,TP num, TAM 2), E2_NUMBOR (Num Bordero,TP char, TAM 6), E2_PROJETO (Projeto,TP char, TAM 6), E2_RATEIO (Rateio,TP char, TAM 1), E2_ACRESC (Acrescimo,TP num, TAM 16), E2_INSS (INSS,TP num, TAM 14), E2_SDACRES (Sld.Acresc.,TP num, TAM 16), E2_DECRESC (Decrescimo,TP num, TAM 16), E2_SDDECRE (Sld.Decresc.,TP num, TAM 16), E2_RETENC (Vl Retencao,TP num, TAM 16), E2_CONTAD (Cta.Contabil,TP char, TAM 20), E2_DEBITO (Conta Deb.,TP char, TAM 20), E2_CCD (C.Custo Deb.,TP char, TAM 9), E2_ITEMD (Item Ctb.Deb,TP char, TAM 9), E2_CLVLDB (Cl.Vlr. Deb.,TP char, TAM 9), E2_CREDIT (Conta Cred.,TP char, TAM 20), E2_CCC (C.Custo Cred,TP char, TAM 9), E2_ITEMC (Item Ctb Crd,TP char, TAM 9), E2_CLVLCR (Cl.Vlr. Cred,TP char, TAM 9), E2_COFINS (COFINS,TP num, TAM 14), E2_PIS (PIS/PASEP,TP num, TAM 14), E2_CSLL (CSLL,TP num, TAM 14), E2_CODBAR (Cod.Barras,TP char, TAM 44), E2_LINDIG (Linha Dig.,TP char, TAM 48), E2_MDPARCE (Num. Parcela,TP char, TAM 2), E2_FORORI (Forn.Orig.,TP char, TAM 6), E2_LOJORI (Loja Orig,TP char, TAM 2), E2_NFELETR (NF Eletr.,TP char, TAM 20), E2_CCUSTO (C. de Custo,TP char, TAM 9), E2_DTBORDE (Dt. Bordero,TP data, TAM 8)) Observação CLIENTE E LOJA são numerais, caso seja informado Nomes lembre de usar o Campo Nome do Cliente ou do Fornecedor.",
    "Compras": "Tabelas disponíveis: SD1010 (D1_FILIAL (Filial,TP char, TAM 2), D1_ITEM (Item NF,TP char, TAM 4), D1_COD (Produto,TP char, TAM 15), D1_UM (Unidade,TP char, TAM 2), D1_QUANT (Quantidade,TP num, TAM 11), D1_VUNIT (Vlr.Unitario,TP num, TAM 14), D1_TOTAL (Vlr.Total,TP num, TAM 14), D1_VALIPI (Vlr.IPI,TP num, TAM 14), D1_VLSLXML (ICMS ST For.,TP num, TAM 14), D1_VALICM (Vlr.ICMS,TP num, TAM 14), D1_OPER (Tp.Oper,TP char, TAM 2), D1_TES (Tipo Entrada,TP char, TAM 3), D1_CF (Cod. Fiscal,TP char, TAM 5), D1_DESC (Desc.Item,TP num, TAM 5), D1_IPI (Aliq. IPI,TP num, TAM 6), D1_PICM (Aliq. ICMS,TP num, TAM 5), D1_PESO (Peso total,TP num, TAM 10), D1_CONTA (C Contabil,TP char, TAM 20), D1_ITEMCTA (Item Conta,TP char, TAM 9), D1_CC (Centro Custo,TP char, TAM 9), D1_FORNECE (Forn/Cliente,TP char, TAM 6), D1_LOJA (Loja,TP char, TAM 2), D1_LOCAL (Armazem,TP char, TAM 2), D1_DOC (Documento,TP char, TAM 9), D1_EMISSAO (DT Emissao,TP data, TAM 8), D1_DTDIGIT (DT Digitacao,TP data, TAM 8), D1_GRUPO (Grupo,TP char, TAM 4), D1_TIPO (Tipo Docto.,TP char, TAM 1), D1_SERIE (Serie,TP char, TAM 3), D1_ICMSRET (ICMS Solid.,TP num, TAM 14), D1_ICMSCOM (ICMS Comple.,TP num, TAM 14), D1_PROJ (Cod. Proj.,TP char, TAM 10), D1_VALFRE (Vlr. Frete,TP num, TAM 14), D1_BASEIRR (Base de IRRF,TP num, TAM 14), D1_ALIQIRR (Aliq. IRRF,TP num, TAM 5), D1_VALIRR (Valor IRRF,TP num, TAM 14), D1_BASEISS (Base de ISS,TP num, TAM 14), D1_ALIQISS (Aliq. ISS,TP num, TAM 5), D1_VALISS (Valor do ISS,TP num, TAM 14), D1_BASEINS (Base de INSS,TP num, TAM 14), D1_ALIQINS (Aliq. INSS,TP num, TAM 5), D1_VALINS (Vlr. do INSS,TP num, TAM 14), D1_CLVL (Classe Valor,TP char, TAM 9), D1_TESDES (Tipo Entrada,TP char, TAM 3), D1_ALFCCMP (FECP Comp.,TP num, TAM 6), D1_VALCOF (Valor Cofins,TP num, TAM 14), D1_VALACRS (Vlr.Acresc.,TP num, TAM 16), D1_ALIQSOL (Aliq ICMS So,TP num, TAM 6), D1_VALCSL (Valor CSLL,TP num, TAM 14), D1_VALPIS (Valor PIS,TP num, TAM 14))",
    "Clientes": "Tabelas disponíveis: SA1010 (A1_FILIAL (Filial,TP char, TAM 2), A1_COD (Codigo,TP char, TAM 6),=, A1_LOJA (Loja,TP char, TAM 2), A1_NOME (Nome,TP char, TAM 40), A1_PESSOA (Fisica/Jurid,TP char, TAM 1), A1_NREDUZ (N Fantasia,TP char, TAM 20), A1_END (Endereco,TP char, TAM 80), A1_BAIRRO (Bairro,TP char, TAM 40), A1_TIPO (Tipo,TP char, TAM 1), A1_EST (Estado,TP char, TAM 2), A1_ESTADO (Nome Estado,TP char, TAM 20), A1_CEP (CEP,TP char, TAM 8), A1_COD_MUN (Cd.Municipio,TP char, TAM 5), A1_MUN (Municipio,TP char, TAM 60), A1_REGIAO (Regiao,TP char, TAM 3), A1_DSCREG (Desc.Região,TP char, TAM 15), A1_NATUREZ (Natureza,TP char, TAM 10), A1_IBGE (Cod.IBGE,TP char, TAM 11), A1_ENDCOB (End.Cobranca,TP char, TAM 40), A1_DDD (DDD,TP char, TAM 3), A1_ENDENT (End.Entrega,TP char, TAM 40), A1_TEL (Telefone,TP char, TAM 15), A1_TRIBFAV (Pes.Tri.Fav.,TP char, TAM 1), A1_ENDREC (End.Recebto,TP char, TAM 40), A1_COMPENT (Comp Entrega,TP char, TAM 50), A1_CGC (CNPJ/CPF,TP char, TAM 14), A1_CONTATO (Contato,TP char, TAM 15), A1_PFISICA (RG/Ced.Estr.,TP char, TAM 18), A1_INSCR (Ins. Estad.,TP char, TAM 18), A1_INSCRM (Ins. Municip,TP char, TAM 18), A1_VEND (Vendedor,TP char, TAM 6), A1_PAISDES (Descr. Pais,TP char, TAM 25), A1_BCO1 (Banco 1,TP char, TAM 3), A1_TPFRET (Tipo Frete,TP char, TAM 1), A1_COND (Cond. Pagto,TP char, TAM 3), A1_DESC (Desconto,TP num, TAM 2))",
    "Fornecedores": "Tabelas disponíveis: SA2010 (A2_GROSSIR (Base Calc IR,TP char, TAM 1),A2_CGC (CNPJ/CPF,TP char, TAM 14), A2_FILIAL (Filial,TP char, TAM 2), A2_COD (Codigo,TP char, TAM 6), A2_LOJA (Loja,TP char, TAM 2), A2_NOME (Razao Social,TP char, TAM 40), A2_NREDUZ (N Fantasia,TP char, TAM 20), A2_END (Endereco,TP char, TAM 40), A2_NR_END (Numero,TP char, TAM 6), A2_BAIRRO (Bairro,TP char, TAM 20), A2_EST (Estado,TP char, TAM 2), A2_CONTPRE (Contrib.Prev,TP char, TAM 1), A2_ESTADO (Nome Estado,TP char, TAM 20), A2_COD_MUN (Cod. Municip,TP char, TAM 5), A2_IBGE (Cod.IBGE,TP char, TAM 11), A2_MUN (Municipio,TP char, TAM 60), A2_CEP (CEP,TP char, TAM 8), A2_TIPO (Tipo,TP char, TAM 1), A2_CX_POST (Caixa Postal,TP char, TAM 5))",
    "Estoque": "Tabelas disponíveis: SB1010 (B1_FILIAL (Filial,TP char, TAM 2), B1_COD (Codigo,TP char, TAM 15), B1_DESC (Descricao,TP char, TAM 30), B1_TIPO (Tipo,TP char, TAM 2), B1_LOCPAD (Armazem Pad.,TP char, TAM 2), B1_GRUPO (Grupo,TP char, TAM 4), B1_PICM (Aliq. ICMS,TP num, TAM 5), B1_IPI (Aliq. IPI,TP num, TAM 5), B1_POSIPI (Pos.IPI/NCM,TP char, TAM 10), B1_ESPECIE (Especie TIPI,TP char, TAM 2), B1_PRV1 (Preco Venda,TP num, TAM 12), B1_CONTA (Cta Contabil,TP char, TAM 20), B1_ORIGEM (Origem,TP char, TAM 1)), SB2010 (B2_FILIAL (Filial,TP char, TAM 2), B2_COD (Produto,TP char, TAM 15), B2_LOCAL (Armazem,TP char, TAM 2), B2_DPROD (Descrição,TP char, TAM 30), B2_QATU (Saldo Atual,TP num, TAM 14), B2_VATU1 (Sld.Atu.,TP num, TAM 14), B2_QEMP (Empenho,TP num, TAM 14), B2_BLOQUEI (Tp.Bloqueio,TP char, TAM 1)); Observação: Lembre-se que o item pode estar em vários armazéns.",
    "Fiscal": "Tabelas disponíveis: SF4010 (F4_FILIAL (Filial, TP char, TAM 2), F4_CODIGO (Cod. do Tipo de Entrada ou Saida composto por 3 digitos normalmente numerais, TP char, TAM 3), F4_TIPO (Tipo do TES, TP char, TAM 1), F4_ICM (Calcula ICMS, TP char, TAM 1), F4_IPI (Calcula IPI, TP char, TAM 1), F4_CREDICM (Cred. ICMS, TP char, TAM 1), F4_CREDIPI (Credita IPI, TP char, TAM 1), F4_DUPLIC (Gera Dupl., TP char, TAM 1), F4_ESTOQUE (Atu.Estoque, TP char, TAM 1), F4_CF (Cod. Fiscal, TP char, TAM 5), F4_TEXTO (Txt Padrao, TP char, TAM 20), F4_PODER3 (Poder Terc., TP char, TAM 1), F4_LFICM (L.Fisc. ICMS, TP char, TAM 1), F4_LFIPI (L.Fiscal IPI, TP char, TAM 1), F4_DESTACA (Destaca IPI, TP char, TAM 1), F4_INCIDE (IPI na base, TP char, TAM 1), F4_ISS (Calculo ISS, TP char, TAM 1), F4_LFISS (L.Fiscal ISS, TP char, TAM 1), F4_NRLIVRO (Nr. Livro, TP char, TAM 1), F4_CONSUMO (Mat.Consumo, TP char, TAM 1), F4_INCSOL (Agrega Solid, TP char, TAM 1), F4_ATUATF (Atual.Ativo, TP char, TAM 1), F4_TESDV (TINDICA QUAL É A TES de entrada que é vinculada a está TES de devolução, TP char, TAM 3), F4_OPEMOV (Op.Movimento, TP char, TAM 2)) TES Significa Tipo de Entrada e Saida, normalmente se pesquisa pelo Codigo da TES",
}

def interpretar_pergunta_com_gpt(modulo, pergunta):
    contexto = MODULOS.get(modulo, "")
    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Você é um assistente especializado na geração de consultas SQL para o banco de dados do ERP Protheus da TOTVS. {contexto} Regras importantes: Use GETDATE() para obter a data atual no SQL Server. Desconsidere linhas marcadas como deletadas usando o comando D_E_L_E_T_ <> '*'. Caso a solicitação seja vaga ou muito curta, inclua expressões que garantam uma consulta funcional. Nem sempre o usuario vai informar dados completos caso necessario busque pela expressão em algumas situações. O formato de datas é composto apenas por numero exemplo 20250101. Use sempre o nome dos campos corretamente para garantir uma consulta valida. Responda apenas com a query SQL, sem usar qualquer explicação ou comentário."},
            {"role": "user", "content": pergunta}
        ],
        max_tokens=350
    )
    query = resposta['choices'][0]['message']['content'].strip()
    # Remover delimitadores de bloco de código
    if query.startswith("```sql") and query.endswith("```"):
        query = query[6:-3].strip()
    return query

def executar_consulta_sql(query):
    try:
        print(f"Executando consulta SQL: {query}")  # Debug
        conn = pyodbc.connect(DB_CONNECTION_STRING)
        cursor = conn.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        conn.close()
        print(f"Resultados: {resultados}")  # Debug
        return resultados, colunas
    except Exception as e:
        print(f"Erro ao executar SQL: {e}")  # Debug
        return str(e), []

def interpretar_resposta_com_gpt(pergunta, resultados, colunas):
    # Se não houver resultados, a IA deve responder de maneira amigável
    if not resultados:
        return "Não encontramos informações para a sua consulta."
    
    # Se a consulta retornar resultados, o modelo pode interpretar de forma mais natural
    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Você é um assistente que responde a perguntas sobre os dados que estão em um ERP da empresa usando resultados de uma pergunta do usuario e uma consulta SQL. A empresa é brasileira e usa Real como moeda."},
            {"role": "user", "content": f"Pergunta: {pergunta}\nResultados: {resultados}\nColunas: {colunas}"}
        ],
        max_tokens=200
    )
    return resposta['choices'][0]['message']['content'].strip()

# Inicializando Flask
app = Flask(__name__)
app.debug = True  # Habilita modo debug

@app.route("/", methods=["GET", "POST"])
def index():
    consulta_sql = ""
    resultados = []
    colunas = []
    erro = ""
    modulo_selecionado = ""
    mensagem_interpretativa = ""
    resposta_natural = ""

    if request.method == "POST":
        modulo_selecionado = request.form["modulo"]
        pergunta = request.form["pergunta"]
        consulta_sql = interpretar_pergunta_com_gpt(modulo_selecionado, pergunta)
        print(f"Consulta gerada pelo GPT: {consulta_sql}")  # Debug
        
        if consulta_sql.lower().startswith("select"):
            resultados, colunas = executar_consulta_sql(consulta_sql)
            if resultados:
                mensagem_interpretativa = f"Encontramos {len(resultados)} registros para a consulta '{consulta_sql}'."
                # Agora, a IA interpreta a resposta de forma natural
                resposta_natural = interpretar_resposta_com_gpt(pergunta, resultados, colunas)
            else:
                mensagem_interpretativa = "Nenhum registro encontrado para a consulta."
                resposta_natural = "Infelizmente, não encontramos dados correspondentes ao seu pedido."

        else:
            erro = "A consulta gerada não é uma consulta SELECT válida."
            resposta_natural = erro

    return render_template("indexV3.html", consulta_sql=consulta_sql, resultados=resultados, colunas=colunas, erro=erro, modulos=MODULOS.keys(), modulo_selecionado=modulo_selecionado, mensagem_interpretativa=mensagem_interpretativa, resposta_natural=resposta_natural)

if __name__ == "__main__":
    app.run(debug=True)
