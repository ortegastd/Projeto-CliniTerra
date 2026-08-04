<h1 align="center">🌿 CliniTerra (Retro Edition)</h1>

<p align="center">
  <em>Um sistema clínico estilo Windows 95, com sons sintetizados, interface nostálgica e auto-formatação.</em>
</p>

---

## 📸 Demonstração do Projeto

*(Adicione seus GIFs aqui na pasta raiz e substitua os nomes dos arquivos abaixo)*

### 1. Painel de Login e Navegação
![Login e Interface](login.gif)

### 2. Efeitos Sonoros e Formatação Automática
![Interação e Sons](interacao.gif)

## 🚀 Sobre o Projeto
O **CliniTerra** é uma aplicação web desenvolvida em **Python** utilizando o framework **Django**. Originalmente um simples sistema de cadastro, ele evoluiu para um sistema completo de gestão de pacientes e agendamentos com uma imersiva interface **Retro Windows 95**, completa com efeitos sonoros em 8-bits renderizados via Web Audio API.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## ✨ Novas Funcionalidades
- **🎨 Interface Nostálgica (Win95):** Botões 3D, fontes de pixel (VT323), janelas clássicas e gradientes retrô, tudo feito com CSS puro.
- **🎹 Efeitos Sonoros Dinâmicos:** Um motor de áudio customizado gera mais de 5 tipos de sons contextuais baseados no que você clica (sucesso, alerta, cancelamento, ticks de rádio, cliques variados), usando 100% matemática (`Web Audio API`).
- **📝 Formatação Automática de Dados:** O sistema formata seu nome (capitalização inteligente ignorando preposições) e a máscara de telefone em tempo real enquanto você digita no formulário.
- **📅 Gestão de Agendamentos:** Permite agendar e visualizar as consultas médicas dos pacientes, bloqueando agendamentos duplicados.
- **👀 Ícones SVG Customizados:** Substituição de emojis modernos por vetores minimalistas criados sob medida (como o olho de ocultar senha na pegada pixel art).
- **🧠 Cálculo Automático de Idade:** A idade do paciente é calculada matematicamente baseada na data de nascimento (com restrição automática do ano).
- **🔥 "FORMAT C:" (Limpeza Completa):** Sistema seguro para deletar cadastros individuais ou formatar completamente o banco de dados em um clique.

## 💻 Como rodar o projeto localmente

Siga os passos abaixo para testar o CliniTerra em sua máquina local.

**1. Clone o repositório e navegue até a sub-pasta do projeto:**
```bash
git clone https://github.com/ortegastd/Projeto-CliniTerra.git
cd Projeto-CliniTerra/Projeto-CliniTerra-main
```

**2. Instale o Django (caso ainda não possua):**
```bash
pip install django
```

**3. Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

**4. Acesse no navegador:**
Abra o seu navegador e acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
