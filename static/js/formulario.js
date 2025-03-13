document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-contato');
    const mensagemErro = document.getElementById('mensagem-erro'); // Elemento para exibir erros

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const mensagem = document.getElementById('mensagem').value;

        const params = new URLSearchParams();
        params.append('nome', nome);
        params.append('email', email);
        params.append('mensagem', mensagem);

        fetch('/enviar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: params.toString()
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert(data.message); // Pode substituir por uma mensagem na página
                form.reset();
            } else {
                if (mensagemErro) {
                    mensagemErro.textContent = data.message;
                } else {
                    alert(data.message);
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