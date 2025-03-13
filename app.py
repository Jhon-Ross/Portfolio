from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import requests
import logging

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
app.logger.setLevel(logging.DEBUG)

# Configuração das variáveis de ambiente
EMAILJS_SERVICE_ID = os.environ.get('EMAILJS_SERVICE_ID')
EMAILJS_TEMPLATE_ID = os.environ.get('EMAILJS_TEMPLATE_ID')
EMAILJS_PRIVATE_KEY = os.environ.get('EMAILJS_PRIVATE_KEY')
EMAILJS_PUBLIC_KEY = os.environ.get('EMAILJS_PUBLIC_KEY')

# Remova a lógica de usar chave pública se a privada estiver ausente.
# A chave privada é necessária para enviar emails via EmailJS.
# Se a chave privada estiver ausente, levante uma exceção no início da aplicação.
if not EMAILJS_PRIVATE_KEY:
    app.logger.error(
        "A chave privada do EmailJS (EMAILJS_PRIVATE_KEY) não foi definida!")
    raise ValueError(
        "A chave privada do EmailJS (EMAILJS_PRIVATE_KEY) não foi definida!")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar_email():
    if request.method == 'POST':
        nome = request.form.get('nome')  # Use .get para evitar KeyError
        email = request.form.get('email')  # Use .get para evitar KeyError
        # Use .get para evitar KeyError
        mensagem = request.form.get('mensagem')

        # Validação básica dos dados (IMPORTANTE!)
        if not nome or not email or not mensagem:
            app.logger.warning("Dados do formulário incompletos.")
            # Bad Request
            return jsonify({'success': False, 'message': 'Por favor, preencha todos os campos do formulário.'}), 400

        payload = {
            'service_id': EMAILJS_SERVICE_ID,
            'template_id': EMAILJS_TEMPLATE_ID,
            'user_id': EMAILJS_PRIVATE_KEY,  # Use SEMPRE a chave PRIVADA
            'template_params': {
                'nome': nome,
                'email': email,
                'mensagem': mensagem
            }
        }

        app.logger.debug(f"Payload: {payload}")

        try:
            response = requests.post(
                'https://api.emailjs.com/api/v1.0/email/send', json=payload)
            app.logger.debug(
                f"Response Status Code: {response.status_code}, Response Text: {response.text}")

            # Analisa a resposta da API EmailJS para identificar erros específicos
            try:
                response_json = response.json()
                if response.status_code != 200:
                    error_message = response_json.get(
                        'error', response.text)  # Pega a mensagem de erro do JSON, se existir
                    app.logger.error(
                        f"Erro ao enviar e-mail (EmailJS): {error_message}")
                    # Retorna o código de status do EmailJS
                    return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {error_message}'}), response.status_code
                else:
                    app.logger.info("E-mail enviado com sucesso!")
                    return jsonify({'success': True, 'message': 'E-mail enviado com sucesso!'}), 200

            except ValueError:  # Erro ao decodificar o JSON
                app.logger.error(
                    f"Erro ao decodificar JSON da resposta: {response.text}")
                return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: Resposta inválida do servidor'}), 500

        except requests.exceptions.RequestException as e:  # Captura erros de conexão
            app.logger.error(f"Erro de conexão ao enviar e-mail: {str(e)}")
            return jsonify({'success': False, 'message': f'Erro de conexão: {str(e)}'}), 500
        except Exception as e:  # Captura outros erros inesperados
            app.logger.error(f"Erro inesperado ao enviar e-mail: {str(e)}")
            return jsonify({'success': False, 'message': f'Erro inesperado: {str(e)}'}), 500

    else:
        # Method Not Allowed
        return jsonify({'success': False, 'message': 'Método não permitido!'}), 405


if __name__ == '__main__':
    app.run(debug=True)
