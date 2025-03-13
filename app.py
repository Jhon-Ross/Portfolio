from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__, static_folder='static', template_folder='templates')

EMAILJS_SERVICE_ID = os.environ.get('EMAILJS_SERVICE_ID')
EMAILJS_TEMPLATE_ID = os.environ.get('EMAILJS_TEMPLATE_ID')
EMAILJS_PUBLIC_KEY = os.environ.get('EMAILJS_PUBLIC_KEY')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/enviar', methods=['POST'])
def enviar_email():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Construa o payload para a API do EmailJS
        payload = {
            'service_id': EMAILJS_SERVICE_ID,
            'template_id': EMAILJS_TEMPLATE_ID,
            'user_id': EMAILJS_PUBLIC_KEY,
            'template_params': {
                'nome': nome,
                'email': email,
                'mensagem': mensagem
            }
        }

        try:
            # Envie a requisição POST para a API do EmailJS
            response = requests.post(
                'https://api.emailjs.com/api/v1.0/email/send', json=payload)

            # Verifique se a requisição foi bem-sucedida
            if response.status_code == 200:
                return jsonify({'success': True, 'message': 'E-mail enviado com sucesso!'})
            else:
                return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {response.text}'})

        except Exception as e:
            print(e)
            return jsonify({'success': False, 'message': f'Erro ao enviar e-mail: {str(e)}'})
    else:
        return jsonify({'success': False, 'message': 'Método não permitido!'})


if __name__ == '__main__':
    app.run(debug=True)
