from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import requests
import logging

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')
app.logger.setLevel(logging.DEBUG)

EMAILJS_SERVICE_ID = os.environ.get('EMAILJS_SERVICE_ID')
EMAILJS_TEMPLATE_ID = os.environ.get('EMAILJS_TEMPLATE_ID')
EMAILJS_PRIVATE_KEY = os.environ.get('EMAILJS_PRIVATE_KEY')
EMAILJS_PUBLIC_KEY = os.environ.get(
    'EMAILJS_PUBLIC_KEY')  # Adicione a chave pública

# Função para determinar qual chave usar


def get_emailjs_user_id():
    if EMAILJS_PRIVATE_KEY:
        return EMAILJS_PRIVATE_KEY
    elif EMAILJS_PUBLIC_KEY:
        return EMAILJS_PUBLIC_KEY
    else:
        app.logger.error(
            "Nenhuma chave do EmailJS (privada ou pública) foi definida!")
        return None  # Ou levante uma exceção


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar_email():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        user_id = get_emailjs_user_id()
        if not user_id:
            return jsonify({'success': False, 'message': 'Erro: Nenhuma chave do EmailJS definida!'})

        payload = {
            'service_id': EMAILJS_SERVICE_ID,
            'template_id': EMAILJS_TEMPLATE_ID,
            'user_id': user_id,  # Use a chave apropriada
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

            if response.status_code == 200:
                return jsonify({'success': True, 'message': 'E-mail enviado com sucesso!'})
            else:
                return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {response.text}'})

        except Exception as e:
            app.logger.error(f"Erro ao enviar e-mail: {str(e)}")
            return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {str(e)}'})
    else:
        return jsonify({'success': False, 'message': 'Método não permitido!'})


if __name__ == '__main__':
    app.run(debug=True)
