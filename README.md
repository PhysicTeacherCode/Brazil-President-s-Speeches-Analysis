# Brazil President's Speeches Analysis:

Uma análise profunda, histórica e orientada a dados dos discursos de posse dos presidentes do Brasil, desde o início da República (1889) até o ano de 2025.

Este projeto utiliza técnicas avançadas de Processamento de Linguagem Natural (PLN), Inteligência Artificial e análise estatística para explorar as mudanças na retórica política brasileira, temas recorrentes e o estilo individual de cada governante através de seus discursos de posse e pronunciamentos oficiais.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Objetivos do Projeto:

- **Carregamento e Estruturação:** Consolidar discursos históricos em um banco de dados relacional (PostgreSQL).
- **Análise Quantitativa:** Comparar a extensão dos discursos e a frequência de palavras ao longo das eras (República Velha, Era Vargas, Regime Militar, Nova República).
- **Modelagem de Tópicos (IA):** Utilizar algoritmos de IA para extrair automaticamente os principais assuntos abordados em cada período histórico.
- **Análise Semântica:** Identificar termos-chave, evolução de temas (como economia, religião e democracia) e realizar a limpeza de dados (remoção de *stopwords*).
- **Visualização de Dados:** Gerar gráficos que facilitem a compreensão da evolução do discurso político brasileiro.

## Tecnologias Utilizadas:

- **Linguagem:** Python 3.x
- **Inteligência Artificial & PLN:** `BERTopic` (Modelagem de tópicos), `scikit-learn` (Cálculo de similaridade de cosseno)
- **Análise de Dados:** `pandas`, `numpy`
- **Visualização:** `matplotlib`, `seaborn`
- **Banco de Dados:** `PostgreSQL`
- **Integração SQL:** `SQLAlchemy`, `psycopg2`
- **Ambiente:** `Jupyter Notebook`
- **Gestão de Configuração:** `python-dotenv`

## Estrutura do Repositório:

```text
├── notebooks/
│   ├── 01-exploratory.ipynb      # Carregamento de dados, contagem de palavras e análises iniciais.
│   └── 02-topic-analyses.ipynb   # Extração automática de tópicos usando BERTopic e IA.
├── src/
│   └── create_dataset.py         # Script Python para criação das tabelas e inserção dos discursos no DB.
├── .gitignore                    # Arquivos ignorados pelo Git (ex: .env).
└── README.md                     # Documentação do projeto.
```

## Como Executar:

### 1. Pré-requisitos:
Certifique-se de ter o Python e o PostgreSQL instalados em sua máquina.

### 2. Configuração do Banco de Dados:
Crie um banco de dados no PostgreSQL e configure as credenciais em um arquivo `.env` na raiz do projeto:
```env
DB_HOST=seu_host
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

### 3. Instalação de Dependências:
```bash
pip install pandas matplotlib sqlalchemy psycopg2 python-dotenv bertopic scikit-learn
```

### 4. Populando o Banco de Dados:
Execute o script para criar as tabelas e inserir os dados:
```bash
python src/create_dataset.py
```

### 5. Executando a Análise:
Abra o Jupyter Notebook e explore as análises:
```bash
jupyter notebook
```

## Insights Extraídos:

Algumas curiosidades já identificadas no projeto:
- **Análise de Tópicos por IA:** Identificação automática de eixos temáticos como "Política e Estado", "Militar e Defesa" e "Economia".
- **O Discurso mais longo:** Fernando Collor de Mello detém o recorde de discurso de posse mais extenso da história republicana.
- **Retórica Religiosa:** O uso do termo "Deus" é analisado de forma relativa ao tamanho do discurso, revelando padrões de oratória específicos em diferentes mandatos.

## Autor:

- **PhysicTeacherCode** - [GitHub](https://github.com/PhysicTeacherCode)

---
*Este projeto foi desenvolvido para fins acadêmicos e de pesquisa histórica.*
