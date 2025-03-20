# Inteligência Artificial - PROTHEUS TOTVS - INTEGRAÇÃO

Este projeto integra o Flask com a API da OpenAI e o banco de dados Protheus, permitindo interpretar perguntas em linguagem natural, convertê-las em consultas SQL válidas e retornar as respostas processadas para o usuário.

## Tecnologias Utilizadas
- Python
- Flask
- OpenAI API
- PyODBC
- Banco de Dados Protheus

## Configuração e Uso

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar um Ambiente Virtual (Opcional)
```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

### 3. Instalar Dependências
```bash
pip install flask openai pyodbc
```

### 4. Configurar as Chaves
Edite o arquivo principal e insira sua chave de API da OpenAI e a string de conexão com o banco de dados Protheus:
```python
openai.api_key = "SUA CHAVE API OPENAI AQUI"
DB_CONNECTION_STRING = "SUA CONEXAO COM BANCO AQUI"
```

### 5. Executar o Servidor
```bash
python app.py
```
O servidor rodará em `http://127.0.0.1:5000/`

## Estrutura do Projeto
```
/
|-- app.py (Arquivo principal)
|-- templates/ (Templates HTML, se aplicável)
|-- static/ (Arquivos estáticos, se aplicável)
|-- requirements.txt (Dependências do projeto)
```

## Módulos e Tabelas do Protheus
A aplicação interage com os seguintes módulos do Protheus:

A aplicação consulta os seguintes módulos e tabelas:

Faturamento: SD2010
Financeiro: SE1010, SE2010
Compras: SD1010
Clientes: SA1010
Fornecedores: SA2010
Estoque: SB1010, SB2010
Fiscal: SF4010

Cada módulo contém informações detalhadas sobre os campos e outros dados relevantes.

## Exemplos de USO

IMAGENS

## Atualizações Futuras

📂 Exportação para XLSX: Permitir a geração de arquivos para grandes volumes de dados, reduzindo o consumo de tokens.
🔗 Integração com Fluig: Facilitar o uso dentro do ambiente corporativo.
📊 Consultas Otimizadas: Melhorar a busca em tabelas agregadas para evitar consumo excessivo de tokens.
🖥 Aumentar alcance expandindo mais tabelas.
🖥 Servidor para DeepSeek (Em análise): Possível customização para aprimorar a ferramenta.

## Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias.

## Licença
Este projeto está sob a licença MIT [LICENSE].
