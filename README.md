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
- No terminal, rodar `python3 nome_do_script.py`

## Projeto front

- utilizamos Next nas configurações padrão (react, TS, Tailwind)

### Configurando

- confirmar the possui node e npm instalados: `node -v` e `npm -v`
- instalar o next.js: `npx create-next-app@latest`
  - a configuração padrão é com Tailwind e Typescript

### Iniciando

- rodar com `npm run dev`
- o arquivo `page.tsx` possui já uma estrutura HTML básica do projeto

### Limpando

- é interessante limpar algumas coisas que não serão usadas nesse projeto.
  1. é possível apenas apagar, se estiver criando um boilerplate
    - projeto > public > todas as imagens dessa pasta
    - projeto > app > `favicon.ico`
  2. é possível ir ja substituindo pelas infos do projeto atual

obs: a pasta public possui os assets estáticos da aplicação, como ícones e imagens


