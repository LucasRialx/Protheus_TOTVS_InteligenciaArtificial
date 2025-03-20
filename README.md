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
git clone https://github.com/LucasRialx/Protheus_TOTVS_InteligenciaArtificial
cd Protheus_TOTVS_InteligenciaArtificial
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
python AssistenteBuscaV6.py
```
O servidor rodará em `http://127.0.0.1:5000/`

## Estrutura do Projeto
```
IA_PROTHEUS
│
├── static
│   ├── css
│        ├── Styles.css
|
├── templates
│   ├── indexV3.HTML
│
├── AssistenteBuscaV6.py


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

![image](https://github.com/user-attachments/assets/0951b095-9d93-4deb-a892-81cf1dd79a4e)
![image](https://github.com/user-attachments/assets/977b44c4-2bde-42e3-8923-1c7d66290181)

![image](https://github.com/user-attachments/assets/da71b852-f48e-4aae-b664-c66c19fcc949)
![image](https://github.com/user-attachments/assets/d32bdfba-1690-4d85-a606-4d4c4db25f06)

![image](https://github.com/user-attachments/assets/cdd4558f-3daa-4a91-b963-9e225de29364)
![image](https://github.com/user-attachments/assets/357cd6d6-5a7a-4e97-ac11-4f7ed36582c9)

E muito mais...

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
