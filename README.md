# Meu Portfólio
<a href="https://jhonrossportfolio-813cd8a5c346.herokuapp.com/#home">Meu Portfólio.</a>

Bem-vindo ao meu portfólio! Este repositório contém o projeto que desenvolvi para demonstrar minhas habilidades em desenvolvimento web, utilizando **HTML**, **CSS** e **JavaScript** no frontend, e **Python** com **Flask** no backend.

## Tecnologias Utilizadas
### Frontend
- **HTML**: Estruturação da página.
- **CSS**: Estilização e design responsivo.
- **JavaScript**: Interatividade e funcionalidades dinâmicas.

### Backend
- **Python**: Lógica de negócio e manipulação de dados.
- **Flask**: Framework para criação da API e gerenciamento de rotas.

## Como Executar o Projeto
Para rodar este projeto localmente, siga os passos abaixo:

### Pré-requisitos
- Python 3.x instalado.
- Git instalado (opcional, para clonar o repositório).

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/Jhon-Ross/Portfolio.git
   ```
2. Navegue até a pasta do projeto:
    ```bash
    cd Portfolio
    ```
3. Crie um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    ```bash
    venv\Scripts\activate
    ```
5. Instale as dependências do backend:
    ```bash
    pip install -r requirements.txt
    ```
6. Inicie o servidor Flask:
    ```bash
    python app.py
    Abra o navegador e acesse http://localhost:5000 para visualizar o frontend.
    ```

### Estrutura do Projeto
```bash
    Portfolio/
├── static/          # Arquivos estáticos (CSS, JS, imagens)
├── templates/       # Arquivos HTML
├── app.py           # Backend em Flask
├── requirements.txt # Dependências do Python
└── README.md        # Documentação do projeto
```

# Para o deploy eu utilizei o Heroku
Para fazer o deploy do seu projeto no Heroku, siga os passos abaixo:

1. Acesse Heroku e crie uma conta gratuita.
<a href="https://www.heroku.com/">Heroku Deploy.</a>

2. Instale o Heroku CLI:

3. Faça login no Heroku:
    No terminal, execute:
    ```bash
    heroku login
    ```
4. Crie um novo app no Heroku:
    Navegue até a pasta do seu projeto e execute:
    ```bash
    heroku create nome-do-seu-app
    ```
5. Configure o Procfile:
    Crie um arquivo chamado Procfile na raiz do projeto (sem extensão) e adicione o seguinte conteúdo:
    ```bash
    web: python app.py
    ```
6. Adicione e commit as mudanças no Git:
    ```bash
    git add .
    git commit -m "Preparando para deploy no Heroku"
    ```
7. Faça o deploy:
    ```bash
    git push heroku main
    ```
8. Abra o app no navegador:
    ```bash
    heroku open
    ```
9. Verifique os logs em caso de erro:
    Se algo der errado, verifique os logs:
    ```bash
    heroku logs --tail
    ```  
## **Licença**
Este projeto está licenciado sob a Licença MIT.
