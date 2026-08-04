<h1 align="center">🌿 CliniTerra</h1>

<p align="center">
  <em>Um sistema de cadastros eficiente, simples e elegante para gerenciamento de clientes.</em>
</p>

---

## 📸 Demonstração do Projeto

![Demonstração do CliniTerra](demo.gif)

## 🚀 Sobre o Projeto
O **CliniTerra** é uma aplicação web desenvolvida em **Python** utilizando o framework **Django**. Seu objetivo é fornecer uma interface rápida e intuitiva para o registro de clientes, com recursos inteligentes como o cálculo automático da idade com base na data de nascimento.

## ✨ Funcionalidades
- **📝 Cadastro de Usuários:** Interface amigável para coletar Nome, Data de Nascimento e Telefone.
- **🧠 Cálculo Automático:** A idade do cliente é calculada automaticamente ao submeter o formulário de cadastro.
- **🗃️ Banco de Dados Local:** Armazenamento seguro de dados utilizando o SQLite3 padrão do Django.
- **📋 Lista de Clientes:** Exibição clara de todos os clientes cadastrados em ordem de entrada.
- **🗑️ Lixeira Individual:** Opção para remover um cadastro específico rapidamente.
- **🔥 Apagar Tudo:** Uma função de "Botão Vermelho" que limpa completamente o banco de dados e reinicia as contagens (útil para testes de homologação).

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.11+, Django 5.0.4
- **Frontend:** HTML5, CSS3 
- **Banco de Dados:** SQLite3

## 💻 Como rodar o projeto localmente

Siga os passos abaixo para testar o CliniTerra em sua máquina local.

**1. Clone o repositório e navegue até a pasta do projeto:**
```bash
git clone https://github.com/ortegastd/Projeto-CliniTerra.git
cd Projeto-CliniTerra
```

**2. Instale o Django (caso ainda não possua):**
```bash
pip install django
```

**3. Aplique as migrações no banco de dados:**
```bash
python manage.py migrate
```

**4. Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

**5. Acesse no navegador:**
Abra o seu navegador e acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
