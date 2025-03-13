from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
app.logger.setLevel(logging.DEBUG)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Servidor SMTP do Gmail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Seu e-mail
app.config['MAIL_PASSWORD'] = os.environ.get(
    'MAIL_PASSWORD')  # Sua senha ou senha de app

# Inicializa o Flask-Mail
mail = Mail(app)

# Verifica se as variáveis de ambiente foram configuradas
if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
    app.logger.error("As credenciais de e-mail não foram configuradas!")
    raise ValueError("As credenciais de e-mail não foram configuradas!")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar_email():
    if request.method == 'POST':
        # Recebe os dados do front-end como JSON
        data = request.json
        nome = data.get('nome')
        email = data.get('email')
        mensagem = data.get('mensagem')

        # Verifica se todos os campos foram preenchidos
        if not nome or not email or not mensagem:
            app.logger.warning("Dados do formulário incompletos.")
            return jsonify({'success': False, 'message': 'Por favor, preencha todos os campos do formulário.'}), 400

        # Cria a mensagem de e-mail
        msg = Message(
            subject=f"Mensagem de {nome}",  # Assunto do e-mail
            sender=app.config['MAIL_USERNAME'],  # Remetente
            # Destinatário (pode ser o mesmo do remetente)
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
            Nome: {nome}
            E-mail: {email}
            Mensagem: {mensagem}
            """
        )

        try:
            # Envia o e-mail
            mail.send(msg)
            app.logger.info("E-mail enviado com sucesso!")
            return jsonify({'success': True, 'message': 'E-mail enviado com sucesso!'}), 200
        except Exception as e:
            app.logger.error(f"Erro ao enviar e-mail: {str(e)}")
            return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {str(e)}'}), 500

    else:
        return jsonify({'success': False, 'message': 'Método não permitido!'}), 405


if __name__ == '__main__':
    app.run(debug=True)
