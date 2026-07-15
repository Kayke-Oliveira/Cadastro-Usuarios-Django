# Sistema de Cadastro de Usuários

Este é um projeto prático desenvolvido com o objetivo de fixar os conceitos fundamentais do framework **Django** (Python) e compreender o funcionamento de um sistema de cadastro (CRUD) integrado a um banco de dados. Para a interface, foi utilizado **Bootstrap** para garantir um layout limpo e (quase) moderno.

---

## Funcionalidades

* **Cadastro de Usuários:** Formulário para inserção e validação de novos usuários.
* **Listagem em Tempo Real:** Exibição dos usuários cadastrados de forma organizada.
* **Interface:** Estilização simplificada e moderna utilizando componentes do Bootstrap.
* **Persistência de Dados:** Integração nativa com o banco de dados SQLite.

---

## Tecnologias Utilizadas

* **Python** (Linguagem de programação)
* **Django** (Framework Web)
* **Bootstrap 5** (Estilização e Responsividade)
* **SQLite** (Banco de dados local)
* **HTML5 / CSS3** (Estruturação e ajustes visuais)

---

## Como rodar o projeto localmente

Siga os passos abaixo para clonar o repositório e executar a aplicação na sua máquina:

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```
### 2. Criar e ativar o ambiente virtual
No linux/maxOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

No windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar as migrações (criar o banco de dados)
```bash
python manage.py migrate
```

### 5. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

## Estrutura Principal do Projeto

**projeto_cad_usuario/:** Configurações principais do Django (URLs, settings, WSGI).

**app_cad_usuario/:** Aplicação responsável pela lógica de cadastro (views, models, rotas locais).

**templates/:** Páginas HTML estruturadas com Bootstrap para renderização dos dados.

## Aprendizados Adquiridos

**Durante o desenvolvimento deste projeto, pude praticar:**

- O padrão MVT (Model-View-Template) do Django.

- Criação de modelos (models.py) e aplicação de migrações (migrations).

- Captura e processamento de dados enviados via requisições POST.

- Integração de bibliotecas CSS externas (Bootstrap) em templates Django.

- Boas práticas de versionamento, configurando o .gitignore e gerenciando dependências com requirements.txt.
