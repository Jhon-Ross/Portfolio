document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-contato');
    const mensagemErro = document.getElementById('mensagem-erro'); // Elemento para exibir erros

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Captura os dados do formulário
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const mensagem = document.getElementById('mensagem').value;

        // Cria um objeto com os dados
        const formData = {
            nome: nome,
            email: email,
            mensagem: mensagem
        };

        // Envia os dados para o back-end (Flask)
        fetch('/enviar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Indica que estamos enviando JSON
            },
            body: JSON.stringify(formData) // Converte os dados para JSON
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert(data.message); // Exibe mensagem de sucesso
                form.reset(); // Limpa o formulário
            } else {
                if (mensagemErro) {
                    mensagemErro.textContent = data.message; // Exibe mensagem de erro na página
                } else {
                    alert(data.message); // Exibe mensagem de erro em um alerta
                }
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            if (mensagemErro) {
                mensagemErro.textContent = 'Ocorreu um erro ao enviar a mensagem. Tente novamente.';
            } else {
                alert('Ocorreu um erro ao enviar a mensagem. Tente novamente.');
            }
        });
    });
});