<h1 align="center">🌿 CliniTerra (Retro Edition)</h1>

<p align="center">
  <em>Um sistema clínico estilo Windows 95, com sons sintetizados, interface nostálgica e auto-formatação.</em>
</p>

---

## 📸 Demonstração do Projeto

![Demonstração do CliniTerra](demo.gif)

## 🚀 Sobre o Projeto
O **CliniTerra** é uma aplicação web desenvolvida em **Python** utilizando o framework **Django**. Originalmente um simples sistema de cadastro, ele evoluiu para um sistema completo de gestão de pacientes e agendamentos com uma imersiva interface **Retro Windows 95**, completa com efeitos sonoros em 8-bits renderizados via Web Audio API.

## ✨ Novas Funcionalidades
- **🎨 Interface Nostálgica (Win95):** Botões 3D, fontes de pixel (VT323), janelas clássicas e gradientes retrô, tudo feito com CSS puro.
- **🎹 Efeitos Sonoros Dinâmicos:** Um motor de áudio customizado gera mais de 5 tipos de sons contextuais baseados no que você clica (sucesso, alerta, cancelamento, ticks de rádio, cliques variados), usando 100% matemática (`Web Audio API`).
- **📝 Formatação Automática de Dados:** O sistema formata seu nome (capitalização inteligente ignorando preposições) e a máscara de telefone em tempo real enquanto você digita no formulário.
- **📅 Gestão de Agendamentos:** Permite agendar e visualizar as consultas médicas dos pacientes, bloqueando agendamentos duplicados.
- **👀 Ícones SVG Customizados:** Substituição de emojis modernos por vetores minimalistas criados sob medida (como o olho de ocultar senha na pegada pixel art).
- **🧠 Cálculo Automático de Idade:** A idade do paciente é calculada matematicamente baseada na data de nascimento (com restrição automática do ano).
- **🔥 "FORMAT C:" (Limpeza Completa):** Sistema seguro para deletar cadastros individuais ou formatar completamente o banco de dados em um clique.

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.11+, Django 5.0.4
- **Frontend:** HTML5, Vanilla CSS, JavaScript Puro (DOM & Web Audio API)
- **Banco de Dados:** SQLite3

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
