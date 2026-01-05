# estocarte

Estocarte é o banco de dados para controle de estoque de produtos e matérias primas da loja [Magia em Bits](https://www.instagram.com/magiaembits)
Scripts para manipulação do banco de dados do Supabase.

[Documentação de python](https://supabase.com/docs/reference/python/initializing) com as referências de código completas.

## Instalação

**virtual enviroment**: `python3 -m venv .venv`

**ativação do virtual enviroment**: `source .ven/bin/activate`

obs: o venv

Dentro do virtual enviroment:

- instalar o supabase: `pip install supabase`
- Para desativar: `deactivate`

## Rodar script

- Criar o arquivo `.env` onde irá colocar as informações do projeto do supabase (url de conexão e chave)
- Criar um arquivo onde fará a conexão com o banco de dados (ex: `supabase_connection.py`)
- Dentro de cada script específico, adicionar `from supabase_connection.py import supabase`
- no terminal, rodar `python3 nome_do_script.py`

