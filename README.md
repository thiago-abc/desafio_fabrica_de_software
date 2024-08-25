# desafio_fabrica_de_software

Projeto Django - Gerenciamento de Artistas e Álbuns
Este projeto Django tem como objetivo criar um sistema para gerenciamento de artistas e álbuns musicais, com integração ao Django Rest Framework para consumo de APIs externas e funcionalidades de edição e exclusão de registros.

Funcionalidades
Cadastro de Artistas: Formulário para cadastro de artistas com campos nome, endereco_pagina, e qtd_integrantes.
Cadastro de Álbuns: Formulário para cadastro de álbuns, com seleção de artistas já cadastrados.
Listagem de Artistas: Página que lista todos os artistas com opções para editar e excluir.
Django Admin: Gestão completa dos registros de artistas e álbuns via interface de administração.
Integração com API Externa: Consumo de API externa para obter gêneros musicais via Django Rest Framework.
Visualização de Detalhes: Página de detalhes de artistas, exibindo também os álbuns vinculados.

Pré-requisitos
Certifique-se de ter os seguintes itens instalados em sua máquina:

Python 3.x
Pip (Python package installer)
Virtualenv (recomendado)

Instalação
Siga as instruções abaixo para instalar e configurar o projeto em sua máquina local.

1. Clone o repositório
https://github.com/thiago-abc/desafio_fabrica_de_software.git

2. Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Realize as migrações do banco de dados
python manage.py migrate

5. Crie um superusuário para acessar o Django Admin
python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento
python manage.py runserver
