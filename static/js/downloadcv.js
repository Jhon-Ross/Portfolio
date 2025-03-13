document.addEventListener('DOMContentLoaded', function() { // Garante que o DOM esteja pronto

    const downloadCvButton = document.getElementById('download-cv-button');

    if (downloadCvButton) { // Verifica se o botão existe

        downloadCvButton.addEventListener('click', function(event) {
            event.preventDefault(); // Impede o link de redirecionar

            const pdfUrl = '/static/assets/pdfs/Jhon-Ross.pdf';
            const link = document.createElement('a');
            link.href = pdfUrl;
            link.download = 'Jhon-Ross-CV.pdf'; // Define o nome do arquivo a ser baixado
            document.body.appendChild(link); // Adiciona o link ao documento
            link.click(); // Simula o clique no link
            document.body.removeChild(link); // Remove o link do documento
        });
    } else {
        console.error('Botão de download do CV não encontrado.');
    }
});